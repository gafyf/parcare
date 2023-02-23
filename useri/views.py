from django.views import generic
from django.urls import reverse_lazy
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth import views, get_user_model
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.contrib.sites.shortcuts import get_current_site
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

from .models import Profil
from clienti.models import Client, Contract, Masina
from plati.models import Factura
from staff.models import Staff
from .forms import LoginForm, UserForm, PasswordResetForm, PasswordResetConfirmForm, PasswordChangeForm, ProfilUpdateForm, UserUpdateForm


def activateEmail(request, user, to_email):
    mail_subject = 'Activeaza contul'
    message = render_to_string('registration/activate_account.html', {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'{user}, mergi la adresa de email {to_email} si activeaza contul')
    else:
        messages.error(request, f'Nu s-a putut trimite email la adresa {to_email}, verifica daca e scrisa corect.')

def register(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active=False
            user.save()
            activateEmail(request, user, form.cleaned_data['email'])
            return redirect('useri:login')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    else:
        form = UserForm()
    return render(request=request, template_name="registration/signup.html", context={'form':form})

def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Multumim pentru confirmarea emailului. Acum te poti loga.')
        return redirect('useri:login')
    else:
        messages.error(request, 'Linkul pentru activare nu e valabil sau a mai fost folosit.')
    return redirect('useri:login')

class LoginView(views.LoginView):
    form_class = LoginForm
    template_name = "registration/login.html"

class LogoutView(views.LogoutView):
    template_name = "registration/logout.html"

class PasswordResetView(views.PasswordResetView):
    email_template_name = "registration/password_reset_email.html"
    form_class = PasswordResetForm
    template_name = "registration/password_reset_form.html"
    success_url = reverse_lazy("useri:password_reset_done")

class PasswordResetConfirmView(views.PasswordResetConfirmView):
    form_class = PasswordResetConfirmForm
    template_name = "registration/password_reset_confirm.html"
    success_url = reverse_lazy("useri:password_reset_complete")

class PasswordResetDoneView(views.PasswordResetDoneView):
    template_name = "registration/password_reset_done.html"

class PasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = "registration/password_reset_complete.html"

class PasswordChangeView(views.PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy("useri:password_change_done")
    template_name= "registration/password_change_form.html"

def password_change_done(request):
    return render(request, 'registration/password_change_done.html')

class ProfilUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/profil_edit.html'
    model = Profil
    form_class = ProfilUpdateForm
    success_url = reverse_lazy("useri:detalii_profil")
    success_message = 'Profil edit OK!'

    def form_valid(self, form):
        form.instance.profil = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('useri:detalii_profil', kwargs={'pk': self.object.pk})
    
class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'registration/user_edit.html'
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy("useri:detalii_profil")
    success_message = 'User edit OK!'

    def get_success_url(self):
        return reverse_lazy('useri:detalii_profil', kwargs={'pk': self.object.profil.pk})
    
    def form_valid(self, form):
        form.instance.profil.user = self.request.user
        return super().form_valid(form)

class DeleteUser(SuccessMessageMixin, generic.DeleteView):
    model = User
    template_name = 'registration/delete_user.html'
    success_message = 'Userul a fost sters.'
    success_url = reverse_lazy('useri:login')

def delete_profil(request, pk):
    template = 'registration/delete_profil.html'
    if request.method == 'POST':
        profil = Profil.objects.get(pk=pk)
        profil.delete()
        messages.warning(request, "Profilul a fost eliminat cu succes!")
        if request.user.is_superuser and request.user.id is not profil.user.id:
            return redirect('parcare:parcare')
        else:        
            return redirect('useri:login')
    return render (request, template)

def detalii_profil(request, pk):
    template = 'useri/detalii_profil.html'
    profil = Profil.objects.get(pk=pk)
    staff = Staff.objects.filter(profil__id=pk)
    data_angajarii = [st.data_angajarii.strftime("%d/%m/%Y") for st in staff]
    client = Client.objects.filter(profil__id=pk)
    data_creare = [cl.data_creare.strftime("%d/%m/%Y") for cl in client]
    contract = Contract.objects.filter(profil__id=pk)
    factura = Factura.objects.filter(profil__id=pk).order_by('-numar').first()
    masina_profil = Masina.objects.filter(profil__id=pk)
    context = {
        'profil': profil,
        'staff': staff,
        'client': client,
        'contract': contract,
        'factura': factura,
        'masina': masina_profil,
        'data_angajarii': data_angajarii,
        'data_creare': data_creare,
    }
    return render (request, template, context)