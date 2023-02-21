from django.conf import settings

from django.shortcuts import render, redirect
import stripe
from django.core.mail import EmailMessage
from django.contrib import messages
# from rest_framework.decorators import api_view
from datetime import timedelta
import datetime

from .forms import CardForm
from clienti.models import Client, Contract
from .models import Factura
from .pdf import factura_client_pdf
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from clienti.views import contract_pdf
from django.core.files.base import ContentFile


stripe.api_key = settings.STRIPE_SECRET_KEY

# @api_view(['POST'])
def plati(request, pk):
    template = 'plati/plati.html'
    user = request.user
    if user.is_authenticated:
        client = Client.objects.get(profil__id=pk)
        cnt = Contract.objects.get(profil__id=pk)
        if request.method == 'POST':
            form = CardForm(request.POST)
            if form.is_valid():
                # Create a token representing the customer's card information
                token = stripe.Token.create(
                    card={
                        "number": form.cleaned_data['card_number'],
                        "exp_month": form.cleaned_data['expiration_month'],
                        "exp_year": form.cleaned_data['expiration_year'],
                        "cvc": form.cleaned_data['cvc'],
                        "name": form.cleaned_data['name']
                    }
                )
                customer_user = stripe.Customer.create(
                        source=token,
                        email=client.profil.email,
                        name=client.profil.prenume,
                        )
                try:
                    if cnt.contract == 'public':
                        abb=50000
                    else:
                        abb=80000
                    
                    charge = stripe.Charge.create(
                        amount=str(abb),
                        currency='ron',
                        description='plata abonamet',
                        customer=customer_user.id,
                        metadata={'client': client, 'client_id': client.id, 'profil_cnp': client.profil.cnp, 'profil_id': client.profil.id, 'contract': cnt.id}, #, 'factura': fact.id
                        receipt_email=customer_user.email
                    )
                        # if payment_successful:
                        # "status": "succeeded",
                    contract = Contract.objects.get(id=charge.metadata.contract)  # (id=cnt.id)
                    if contract.id == cnt.id:
                        if contract.data_expirare.date() <= datetime.date.today():
                            contract.data_expirare = datetime.date.today() + timedelta(days=30)
                            contract.platit = True
                            contract.save()
                        else:
                            contract.data_expirare += timedelta(days=30)
                            contract.platit = True
                            contract.save()
                        
                        factura_numar = Factura.objects.order_by('-numar').first()
                        if factura_numar:
                            factura_numar.numar += 1
                        else:
                            factura_numar = Factura(numar=1)

                        factura_client_dict = {
                            'nume':client.profil.nume,
                            'prenume':client.profil.prenume,
                            'cnp':client.profil.cnp,
                            'judet':client.profil.judet,
                            'oras':client.profil.oras,
                            'adresa':client.profil.adresa,
                            'email':client.profil.email,
                            'telefon':client.profil.telefon,
                            'contract_numar':contract.numar,
                            'contract':contract.contract,
                            'numar':factura_numar.numar,
                        }
                        factura_client = Factura.objects.create(profil=cnt.profil, numar=factura_numar.numar)
                        factura_pdf = factura_client_pdf(factura_client_dict).getvalue()
                        pdf_file = ContentFile(factura_pdf)
                        factura_client.pdf.save('contract.pdf', pdf_file)
                        factura_client.save()

                        file_to_be_sent = contract_pdf(request, contract.pk).getvalue()
                        subject = 'Documente Abonament Parcare'
                        body = 'Bună ziua! \n''\n' 'Vă mulțumim pentru achitarea abonamentului dvs. la parcare. Acesta este valabil pentru 30 de zile. \n''\n' 'Vă informăm că în acest email veți găsi atașate contractul și factura aferente acestui abonament. \n''\n' 'Vă dorim o zi frumoasă! \n''\n' 'Echipa de la Parcare.'
                        email = EmailMessage(
                            subject,
                            body,
                            from_email=settings.EMAIL_FROM,
                            to=[customer_user.email],
                        )
                        if cnt.data_creare == datetime.date.today():
                            email.attach('factura.pdf', factura_pdf, 'application/pdf')
                            email.attach('contract.pdf', file_to_be_sent, 'application/pdf')
                        else:
                            email.attach('factura.pdf', factura_pdf, 'application/pdf')

                        if email.send():
                            messages.success(request, f'{client.profil.nume} {customer_user.name}, mergi la adresa de email {client.profil.email} pentru a descarca factura si contractul')
                        else:
                            messages.error(request, f'Nu s-a putut trimite email la adresa {client.profil.email}, verifica daca e scrisa corect.')
                        
                        return redirect ('useri:detalii_profil', client.profil.id)
                    else:
                        messages.error(request, 'Eroare de comunicare serviciu plati.')
                except stripe.error.CardError as e:
                    return messages.error(request, {'error': str(e)})
                    # return render(request, 'plati_2.html', {'error': str(e)})
            else:
                messages.warning(request, "Formular incomplet sau incorect.")
        else:
            form = CardForm()
            if cnt.contract == 'public':
                total = 500.00
                percentage = 10
                pret_lung = total / (1 + percentage / 100)
                pret = round(pret_lung, 2) # 450.45
                tva = round(total - pret, 2)
            else:
                total = 800.00
                percentage = 10
                pret_lung = total / (1 + percentage / 100)
                pret = round(pret_lung, 2) # 727.27
                tva = round(total - pret, 2)
        return render(request, template, {'form': form, 'client': client, 'cnt': cnt,
            'pret': pret, 'tva': tva, 'total': total})
    else:
        return render(request, template)

# # @api_view(['GET'])
# def plata_ok(request, id):
#     pdf = contract_pdf
#     try:
#         payment = stripe.Charge.retrieve(id)
#         contract = Contract.objects.get(profil__id=payment.metadata.profil_id)
#         print(contract)
#         context = {'payment': payment, 'pdf':pdf, 'contract':contract}
#         return render(request, 'plati/plata_ok.html', context)
#     except stripe.error.InvalidRequestError as e:
#         return render(request, 'plati/plati_2.html', {'error': str(e)})

def facturi(request, pk):
    template = 'plati/facturi.html'
    facturi = Factura.objects.filter(profil__id=pk)
    return render(request, template, {'facturi': facturi})

def factura_pdf(request, pk):
    user = request.user
    factura = get_object_or_404(Factura, pk=pk)
    if user.is_authenticated and (user.is_superuser or (user.is_staff or user.profil.id == factura.profil.id)):
        pdf_file = factura.pdf
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{factura.numar} - {factura.profil}.pdf"'
        return response
    else:
        return HttpResponse("Nu esti autorizat pt factura PDF")

def email_plata(request):
    template = 'plati/email_plata.html'
    return render(request, template)
