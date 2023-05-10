from django.shortcuts import render, redirect
from django.contrib import messages
from django.db.models import Q
from useri.models import Profil
from clienti.models import Masina
from .models import Staff
from .forms import StaffNouForm
from clienti.forms import MasinaForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from parcare.views import render_to_pdf
from clienti.views import creaza_parola
from django.conf import settings
from django.core.mail import EmailMessage
from django.shortcuts import get_object_or_404
from django.core.files.base import ContentFile
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def staff_contract(request, pk):
    user = request.user
    if user.is_authenticated and (user.is_superuser or (user.is_staff and str(user.profil.id)==pk)):
        contract = get_object_or_404(Staff, profil__pk=pk)
        pdf_file = contract.pdf
        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'filename="{contract.numar} - {contract.profil}.pdf"'
        return response
    else:
        return HttpResponse(_("Nu esti autorizat pt contract Staff PDF"))

def contract(staff_contract_dict):
    pdf = render_to_pdf('staff/contract.html', staff_contract_dict)
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = "filename=contract.pdf" #attachment; 
    return response

def staff_nou(request, pk):
    template = 'staff/staff_nou.html'
    user = request.user
    if user.is_authenticated and user.is_superuser and str(user.profil.id)==pk:
        staff_form = StaffNouForm()
        parola_staff = creaza_parola()
        if request.method == 'POST':
            staff_form = StaffNouForm(request.POST)
            if staff_form.is_valid():
                staff_exista = Staff.objects.filter(Q(profil__user__username=staff_form.cleaned_data['nume'] + staff_form.cleaned_data['prenume']) | Q(profil__cnp=staff_form.cleaned_data['cnp']) | Q(profil__email=staff_form.cleaned_data['email']))
                if staff_exista.exists():
                    messages.warning(request, _("Username, cnp sau email existente in baza de date. Introdu alte date."))
                    print('test username, cnp si email', staff_exista, 'EXISTENT!!!')
                else:
                    print(staff_form.cleaned_data)
                    user_staff = User.objects.create_user(
                        username = staff_form.cleaned_data['nume'] + staff_form.cleaned_data['prenume'],
                        first_name = staff_form.cleaned_data['prenume'],
                        last_name = staff_form.cleaned_data['nume'],
                        email = staff_form.cleaned_data['email'],
                        is_staff=True
                        )
                    print('profil test', user_staff)
                    user_staff.set_password(parola_staff)
                    user_staff.save()

                    profil_staff = Profil.objects.filter(user=user_staff).update(
                        cnp=staff_form.cleaned_data['cnp'],
                        judet=staff_form.cleaned_data['judet'],
                        oras=staff_form.cleaned_data['oras'],
                        adresa=staff_form.cleaned_data['adresa'],
                        telefon=staff_form.cleaned_data['telefon']
                        )
                    print('profil test', profil_staff)

                    contract_numar = Staff.objects.order_by('-numar').first()
                    if contract_numar:
                        contract_numar.numar += 1
                    else:
                        contract_numar = Staff(numar=1)

                    staff_contract_dict = {
                        'nume': user_staff.last_name,
                        'prenume': user_staff.first_name,
                        'cnp':staff_form.cleaned_data['cnp'],
                        'judet':staff_form.cleaned_data['judet'],
                        'oras':staff_form.cleaned_data['oras'],
                        'adresa':staff_form.cleaned_data['adresa'],
                        'functie':staff_form.cleaned_data['functie'],
                        'numar':contract_numar.numar,
                        'data_angajarii':timezone.now().strftime("%d/%m/%Y")
                    }

                    staff = Staff(
                        profil=user_staff.profil,
                        functie=staff_form.cleaned_data['functie'],
                        numar=contract_numar.numar
                        )
                    staff_contract = contract({'staff_contract_dict':staff_contract_dict}).getvalue()
                    pdf_file = ContentFile(staff_contract)
                    staff.pdf.save('contract.pdf', pdf_file)
                    staff.save()
                    print('staff test', staff)

                    masina, m = Masina.objects.get_or_create(
                        marca=staff_form.cleaned_data['marca'],
                        model=staff_form.cleaned_data['model'],
                        numar=staff_form.cleaned_data['numar'],
                        culoare=staff_form.cleaned_data['culoare'],
                        combustibil=staff_form.cleaned_data['combustibil']
                        )
                    masina.p_json.update({len(masina.p_json)+1:str(user_staff.id)})
                    print('masina test', m)
                    masina.profil.add(user_staff.profil)
                    masina.save()

                    subject = _('Cont Staff creat cu succes!')
                    body = _('\n''\n' 'User dumneavoastra este: ' + user_staff.username + '\n''\n' 'Parola dumneavoastra este: ' + parola_staff + '\n''\n' 'Acum va puteti loga si le puteti schimba din setari user')
                    email = EmailMessage(
                        subject,
                        body,
                        from_email=settings.EMAIL_FROM,
                        to=[user_staff.email],
                    )
                    email.attach('contract.pdf', staff_contract, 'application/pdf')
                    if email.send():
                        messages.success(request, _('Angajat nou introdus cu succes!!!'))
                    else:
                        messages.error(request, _(f'Nu s-a putut trimite email la adresa {user_staff.email}, verifica daca e scrisa corect.'))
                    return redirect ('parcare:parcare')
            else:
                messages.warning(request, _("Nu ai completat toate campurile obligatorii."))
                msg = _('Formularul nu e valid. Campuri necompletate.')
                print(msg)
        else:
            staff_form = StaffNouForm()
        context = {'staff_form': staff_form}
        return render(request, template, context)
    else:
        return HttpResponse(_("Nu esti autorizat sa introduci un angajat nou."))

def masina_noua(request, pk):
    template = 'staff/masina_noua.html'
    user = request.user
    if user.is_authenticated and (user.is_superuser or str(user.profil.id)==pk):
        masina_form = MasinaForm
        profil = Profil.objects.get(pk=pk)
        if request.method == 'POST':
            masina_form = MasinaForm(request.POST)
            if masina_form.is_valid():
                masina_exista = Masina.objects.filter(numar=masina_form.cleaned_data['numar'])
                if masina_exista.exists():
                    messages.warning(request, _('Masina exista in baza de date'))
                    print('Masina cu numarul',  masina_exista, 'exista in baza de date')
                else:
                    masina = Masina(
                        marca=masina_form.cleaned_data['marca'],
                        model=masina_form.cleaned_data['model'],
                        numar=masina_form.cleaned_data['numar'],
                        culoare=masina_form.cleaned_data['culoare'],
                        combustibil=masina_form.cleaned_data['combustibil']
                    )
                    masina.p_json.update({len(masina.p_json)+1:str(masina.id)})
                    masina.save()
                    masina.profil.add(profil)
                    print('masina', masina, 'inregistrata cu succes')
                    return redirect ('useri:detalii_profil', pk=profil.id)
            else:
                messages.warning(request, _("Nu ai completat toate campurile obligatorii."))
                msg = _('Formularul nu e valid. Campuri necompletate.')
                print(msg)
        context = {
            'masina_form': masina_form
        }
        response = render(request, template, context)
        return response
    else:
        return HttpResponse(_("Nu esti autorizat sa introduci masina noua."))

