from django.contrib import messages
from django.shortcuts import render, redirect
from .models import Client, Contract, Masina
from .forms import ClientNouForm
from useri.models import Profil
from plati.models import Factura
from django.contrib.auth.models import User
from datetime import timedelta
from django.http import HttpResponse
import datetime
from django.utils import timezone
from django.core.files.base import ContentFile

import string
import random
from django.conf import settings
from django.core.mail import EmailMessage
from plati.pdf import factura
from django.shortcuts import get_object_or_404
from parcare.views import render_to_pdf
from django.utils.translation import gettext_lazy as _


def creaza_parola(length=10, characters=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(characters) for i in range(length))

def contract_pdf_view(contract_client_dict):
    pdf = render_to_pdf('parcare/pdf.html', contract_client_dict)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "filename=contract abonament.pdf" #attachment; 
    return response

def contract_pdf(request, pk):
    user = request.user
    contract = get_object_or_404(Contract, pk=pk)
    if user.is_authenticated and (user.is_superuser or (user.is_staff or user.profil.id == contract.profil.id)):
        pdf_file = contract.pdf
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{contract.numar} - {contract.profil}.pdf"'
        return response
    else:
        return HttpResponse(_("Nu esti autorizat pt contract PDF"))

def client_nou(request, pk):
    template = 'clienti/client_nou.html'
    user = request.user
    if user.is_superuser or user.is_staff:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR', '')
        user_ip = x_forwarded_for.split(',')[0] if x_forwarded_for else request.META.get('REMOTE_ADDR')
        if user_ip == '127.0.0.1':
            print('test user local host OK!')
            parola_client = creaza_parola()
            client_form = ClientNouForm()
            if request.method == 'POST':
                client_form = ClientNouForm(request.POST)
                if client_form.is_valid():
                    client_exista = Client.objects.filter(profil__email=client_form.cleaned_data['email'], profil__cnp=client_form.cleaned_data['cnp'], profil__user__username = client_form.cleaned_data['nume'] + client_form.cleaned_data['cnp'])
                    if client_exista.exists():
                        messages.warning(request, _("Adresa email, user si cnp existente in baza de date. Introdu alte date."))
                        print('test email & cnp', client_exista, 'EXISTENT!!!')
                    else:
                        print(client_form.cleaned_data)
                        user_client = User.objects.create_user(
                            username = client_form.cleaned_data['nume'] + client_form.cleaned_data['cnp'],
                            first_name = client_form.cleaned_data['prenume'],
                            last_name = client_form.cleaned_data['nume'],
                            email = client_form.cleaned_data['email']
                            )
                        print('username test', user_client)
                        user_client.set_password(parola_client)
                        user_client.save()
                        profil_client = Profil.objects.filter(user=user_client).update(
                            cnp=client_form.cleaned_data['cnp'],
                            judet=client_form.cleaned_data['judet'],
                            oras=client_form.cleaned_data['oras'],
                            adresa=client_form.cleaned_data['adresa'],
                            telefon=client_form.cleaned_data['telefon']
                            )
                        print('profil nr asociat la user client test', profil_client)
                        client = Client(
                            profil=user_client.profil,
                            nr_permis=client_form.cleaned_data['nr_permis'],
                            categ_permis=client_form.cleaned_data['categ_permis']
                            )
                        print('client test', client)
                        client.save()
                        masina, m = Masina.objects.get_or_create(
                            marca=client_form.cleaned_data['marca'],
                            model=client_form.cleaned_data['model'],
                            numar=client_form.cleaned_data['numar'],
                            culoare=client_form.cleaned_data['culoare'],
                            combustibil=client_form.cleaned_data['combustibil']
                            )
                        masina.p_json.update({len(masina.p_json)+1:str(user_client.profil.id)})
                        print('masina test', m)
                        masina.profil.add(user_client.profil)
                        masina.save()

                        contract_numar = Contract.objects.order_by('-numar').first()
                        if contract_numar:
                            contract_numar.numar += 1
                        else:
                            contract_numar = Contract(numar=1)

                        contract_client_dict = {
                            'prenume':client_form.cleaned_data['prenume'],
                            'nume':client_form.cleaned_data['nume'],
                            'email':client_form.cleaned_data['email'],
                            'cnp':client_form.cleaned_data['cnp'],
                            'judet':client_form.cleaned_data['judet'],
                            'oras':client_form.cleaned_data['oras'],
                            'adresa':client_form.cleaned_data['adresa'],
                            'telefon':client_form.cleaned_data['telefon'],
                            'numar':contract_numar.numar,
                            'contract':client_form.cleaned_data['contract'],
                            'data_creare':timezone.now().strftime("%d/%m/%Y"),
                            'nr_permis':client_form.cleaned_data['nr_permis'],
                            'categ_permis':client_form.cleaned_data['categ_permis'],
                            'masina':masina
                        }

                        contract_client = Contract.objects.create(
                            profil=user_client.profil,
                            data_expirare = datetime.date.today() + timedelta(days=30),
                            platit = True,
                            contract=client_form.cleaned_data['contract'],
                            numar=contract_numar.numar
                            )

                        contract_client_pdf = contract_pdf_view({'contract_client_dict': contract_client_dict}).getvalue()
                        pdf_file = ContentFile(contract_client_pdf)
                        contract_client.pdf.save('contract.pdf', pdf_file)
                        contract_client.save()
                        print('contract test', contract_client)

                        factura_numar = Factura.objects.order_by('-numar').first()
                        if factura_numar:
                            factura_numar.numar += 1
                        else:
                            factura_numar = Factura(numar=1)
                        
                        factura_client_dict = {
                            'nume':client_form.cleaned_data['nume'],
                            'prenume':client_form.cleaned_data['prenume'],
                            'cnp':client_form.cleaned_data['cnp'],
                            'judet':client_form.cleaned_data['judet'],
                            'oras':client_form.cleaned_data['oras'],
                            'adresa':client_form.cleaned_data['adresa'],
                            'email':client_form.cleaned_data['email'],
                            'telefon':client_form.cleaned_data['telefon'],
                            'contract':contract_client.numar,
                            'numar':factura_numar.numar
                        }

                        factura_client = Factura.objects.create(profil=user_client.profil, numar=factura_numar.numar)
                        factura_pdf = factura(factura_client_dict).getvalue()
                        pdf_file = ContentFile(factura_pdf)
                        factura_client.pdf.save('contract.pdf', pdf_file)
                        factura_client.save()

                        subject = _('Cont Client creat cu succes!')
                        body = _('\n''\n' 'User dumneavoastra este: ' + user_client.username + '\n''\n' 'Parola dumneavoastra este: ' + parola_client + '\n''\n' 'Acum va puteti loga si le puteti schimba din setari user')
                        email = EmailMessage(
                            subject,
                            body,
                            from_email=settings.EMAIL_FROM,
                            to=[client_form.cleaned_data['email']],
                        )
                        email.attach('contract.pdf', contract_client_pdf, 'application/pdf')
                        email.attach('factura.pdf', factura_pdf, 'application/pdf')
                        if email.send():
                            messages.success(request, _(f'{client.profil.nume} {client.profil.prenume}, mergi la adresa de email {user_client.email} pentru a descarca factura si contractul'))
                        else:
                            messages.error(request, _(f'Nu s-a putut trimite email la adresa {user_client.email}, verifica daca e scrisa corect.'))
                        messages.info(request, _('Client nou introdus cu succes!!!'))
                        return redirect ('parcare:parcare')
                else:
                    messages.warning(request, _("Nu ai completat toate campurile obligatorii."))
                    msg = _('Formularul nu e valid. Campuri necompletate.')
                    print(msg)
            
            else:
                client_form = ClientNouForm()
                messages.warning(request, _("ATENTIE! PLATA LA GHISEU INAINTEA VALIDARII!"))
        else:
            return HttpResponse(_("NU ESTI CONECTAT LA SERVERUL LOCAL."))
    else:
        if user.is_authenticated:
            profil = Profil.objects.get(pk=pk)
            client_form = ClientNouForm(initial={'nume': profil.nume, 'prenume': profil.prenume, 'email': profil.email, 'cnp': profil.cnp, 'judet': profil.judet, 'oras': profil.oras, 'adresa': profil.adresa, 'telefon': profil.telefon})
        else:
            client_form = ClientNouForm()
        if request.method == 'POST':
            client_form = ClientNouForm(request.POST)
            if client_form.is_valid(): # save form data to variables
                client_exista = Client.objects.filter(profil__email=client_form.cleaned_data['email'], profil__cnp=client_form.cleaned_data['cnp'])
                if client_exista.exists():
                    messages.warning(request, _("Adresa email si cnp existente in baza de date. Introdu alte date."))
                    print('test email & cnp', client_exista, 'EXISTENT!!!')
                else:
                    print(client_form.cleaned_data)
                    profil_client = Profil.objects.filter(pk=profil.pk).update(
                            prenume=client_form.cleaned_data['prenume'],
                            nume=client_form.cleaned_data['nume'],
                            email=client_form.cleaned_data['email'],
                            cnp=client_form.cleaned_data['cnp'],
                            judet=client_form.cleaned_data['judet'],
                            oras=client_form.cleaned_data['oras'],
                            adresa=client_form.cleaned_data['adresa'],
                            telefon=client_form.cleaned_data['telefon']
                    )
                    print('profil test', profil_client)

                    client = Client(
                        profil=profil,
                        nr_permis=client_form.cleaned_data['nr_permis'],
                        categ_permis=client_form.cleaned_data['categ_permis']
                        )
                    print('client test', client)
                    client.save()

                    masina, m = Masina.objects.get_or_create(
                        marca=client_form.cleaned_data['marca'],
                        model=client_form.cleaned_data['model'],
                        numar=client_form.cleaned_data['numar'],
                        culoare=client_form.cleaned_data['culoare'],
                        combustibil=client_form.cleaned_data['combustibil']
                        )
                    # masina.clienti.update({str(masina.id):str(profil.id)})
                    masina.p_json.update({len(masina.p_json)+1:str(profil.id)})
                    print('masina test', m)
                    masina.profil.add(profil)
                    masina.save()

                    contract_numar = Contract.objects.order_by('-numar').first()
                    if contract_numar:
                        contract_numar.numar += 1
                    else:
                        contract_numar = Contract(numar=1)

                    contract_client_dict = {
                        'prenume':client_form.cleaned_data['prenume'],
                        'nume':client_form.cleaned_data['nume'],
                        'email':client_form.cleaned_data['email'],
                        'cnp':client_form.cleaned_data['cnp'],
                        'judet':client_form.cleaned_data['judet'],
                        'oras':client_form.cleaned_data['oras'],
                        'adresa':client_form.cleaned_data['adresa'],
                        'telefon':client_form.cleaned_data['telefon'],
                        'numar':contract_numar.numar,
                        'contract':client_form.cleaned_data['contract'],
                        'data_creare':timezone.now().strftime("%d/%m/%Y"),
                        'nr_permis':client_form.cleaned_data['nr_permis'],
                        'categ_permis':client_form.cleaned_data['categ_permis'],
                        'masina':masina
                    }

                    contract_client = Contract.objects.create(
                        profil=profil,
                        contract=client_form.cleaned_data['contract'],
                        numar=contract_numar.numar
                        )

                    contract_client_pdf = contract_pdf_view({'contract_client_dict': contract_client_dict}).getvalue()
                    pdf_file = ContentFile(contract_client_pdf)
                    contract_client.pdf.save('contract.pdf', pdf_file)
                    contract_client.save()
                    print('contract test', contract_client)

                    messages.info(request, _('Contract creat cu succes!'))
                    return redirect ('plati:plati', pk=profil.id)
            else:
                messages.warning(request, _("Nu ai completat toate campurile obligatorii."))
                msg = _('Formularul nu e valid. Campuri necompletate.')
                print(msg)
        else:
            client_form = ClientNouForm(initial={'nume': profil.nume, 'prenume': profil.prenume, 'email': profil.email, 'cnp': profil.cnp, 'judet': profil.judet, 'oras': profil.oras, 'adresa': profil.adresa, 'telefon': profil.telefon})
    context = {'client_form': client_form}
    return render(request, template, context)

def masina(request, pk, masina_id):
    profil = get_object_or_404(Profil, pk=pk)
    masina = get_object_or_404(Masina, pk=masina_id)
    template = 'clienti/masina.html'
    return render (request, template, {'masina': masina, 'profil': profil})

def del_masina(request, pk, masina_id):
    template = 'clienti/del_masina.html'
    user = request.user
    profil = get_object_or_404(Profil, pk=pk)
    masina = get_object_or_404(Masina, pk=masina_id)
    if user.is_authenticated and (user.is_superuser or str(user.profil.id)==pk):
        if request.method == 'POST':
            profil.masini.remove(masina)
            print('masina', masina, 'eliminata cu succes')
            return redirect ('useri:detalii_profil', pk=profil.id)
    else:
        return HttpResponse(_("Nu esti autorizat sa elimini masina."))
    context = {'masina': masina, 'profil': profil}
    response = render(request, template, context)
    return response
