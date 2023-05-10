from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import Profil
from django.utils.translation import gettext_lazy as _


class UserForm(UserCreationForm):
    username = forms.CharField(label=_('User:'), help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('User')}))
    email = forms.EmailField(label='Email:', help_text=None, widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': _('email@exemplu.ro')}))
    first_name = forms.CharField(label=_('Prenume:'), help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Prenume')}),)
    last_name = forms.CharField(label=_('Nume:'), help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nume')}))
    password1 = forms.CharField(label=_('Parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Parola')}))
    password2 = forms.CharField(label=_('Confirmare Parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Confirmare parola')}))
    
    class Meta:
        model = User
        #exclude = ('password',)
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label=_('User:'), help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('User')}),)
    password = forms.CharField(label=_('Parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Parola')}))

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email:', help_text=None, widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('email@exemplu.ro')}))

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label=_('Noua parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('Noua parola')}))
    new_password2 = forms.CharField(label=_('Confirmare parola noua:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Confirmare parola')}))

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label=_('Parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('Parola actuala')}))
    new_password1 = forms.CharField(label=_('Noua parola:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Noua parola')}))
    new_password2 = forms.CharField(label=_('Confirmare parola noua:'), help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': _('Confirmare parola')}))

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label=_('User:'), help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': _('User')}))
    class Meta:
        model = User
        fields = ['username']
 

class ProfilUpdateForm(forms.ModelForm):
    nume = forms.CharField(label=_('Nume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nume')}))
    prenume = forms.CharField(label=_('Prenume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Prenume')}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': _('Email')}))
    cnp = forms.CharField(label=_('CNP'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('CNP')}))
    judet = forms.CharField(label=_('Judet'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Judet')}))
    oras = forms.CharField(label=_('Oras'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Oras')}))
    adresa = forms.CharField(label=_('Adresa'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Adresa')}))
    telefon = forms.CharField(label=_('Telefon'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telefon')}))
    imagine = forms.ImageField(label=_('Imagine'), widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': _('Imagine')}))

    class Meta:
        model = Profil
        fields = ['nume', 'prenume', 'email', 'cnp', 'judet', 'oras', 'adresa', 'telefon', 'imagine']
