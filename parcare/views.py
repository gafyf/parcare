import io

from django.template.loader import get_template
from xhtml2pdf import pisa

from django.shortcuts import render
from django.http import HttpResponse

from .models import Imagine
from useri.models import Profil
from clienti.models import Client, Masina, Contract
from staff.models import Staff
from .forms import ImagineForm
from plati.models import Factura

def tarife(request):
    template = 'parcare/tarife.html'
    return render(request, template)

def tarife_ora(request):
    template = 'parcare/tarife_ora.html'
    return render(request, template)

def abonamente(request):
    template = 'parcare/abonamente.html'
    user = request.user
    if user.is_authenticated and (user.is_staff or user.is_superuser):
        return render(request, template)
    else:
        if user.is_authenticated:
            if user.profil in Client.objects.all():
                client = Client.objects.get(profil__id=user.profil.id)
                if user.is_authenticated and client.profil.id==user.profil.id:
                    contract = Contract.objects.get(profil__id=user.profil.id)
                    return render(request, template, {'client': client, 'contract': contract})
                else:
                    return render(request, template)
            else:
                return render(request, template)
        else:
            return render(request, template)

def carduri(request):
    template = 'parcare/carduri.html'
    return render(request, template)

def render_to_pdf(template_path, context_dict={}):
    template = get_template(template_path)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument( 
        src=io.BytesIO(html.encode('UTF-8')),
        dest=result,
        encoding='UTF-8'
    )
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    if pdf.err:
       return HttpResponse('EROARE REDARE DOCUMENT PDF')
    return None

def termeni_si_conditii(request):
    pdf = render_to_pdf('parcare/termeni_si_conditii.html')
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "filename=termeni_si_conditii.pdf" #attachment; 
    return response

def info_client_contract_pdf(request):
    pdf = render_to_pdf('parcare/pdf_info.html')
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "filename=contract.pdf" 
    return response

def servicii(request):
    template = 'parcare/servicii.html'
    return render(request, template)

def contact(request):
    template = 'parcare/contact.html'
    return render(request, template)
    
def galerie(request):
    imagini = Imagine.objects.all()
    if request.user.is_superuser:
        if request.method == 'POST':
            form = ImagineForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                return render(request, 'parcare/galerie.html', {'form': form, 'imagini': imagini})
        else:
            form = ImagineForm()
            return render(request, 'parcare/galerie.html', {'form': form, 'imagini': imagini})
    else:
        return render(request, 'parcare/galerie.html', {'imagini': imagini})
    
def parcare(request):
    template = 'parcare/parcare.html'
    masina = Masina.objects.all()
    masini = Masina.profil.through.objects.all()
    staff = Staff.objects.all()
    s = Staff.objects.filter(profil__nume__istartswith='t')
    print(s)
    contract = Contract.objects.all()
    profil = Profil.objects.all()
    client = Client.objects.all()
    fact = Factura.objects.all()
    context = {
        'fact': fact,
        'profil': profil,
        'masini': masini,
        'masina': masina,
        'contract': contract,
        'client': client,
        'staff': staff,
    }
    response = render(request, template, context)
    return response
