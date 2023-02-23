from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
from .models import Profil

class UserForm(UserCreationForm):
    username = forms.CharField(label='User:', help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'Nume User'}),)
    email = forms.EmailField(label='Email:', help_text=None, widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'email@exemplu.ro'}),)
    first_name = forms.CharField(label='Prenume:', help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),)
    last_name = forms.CharField(label='Nume:', help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),)
    password1 = forms.CharField(label='Parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Parola'}),)
    password2 = forms.CharField(label='Confirmare Parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Confirmare parola'}),)
    
    class Meta:
        model = User
        #exclude = ('password',)
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']
        
class LoginForm(AuthenticationForm):
    username = forms.CharField(label='User:', help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'Nume User'}),)
    password = forms.CharField(label='Parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Parola'}),)

class PasswordResetForm(PasswordResetForm):
    email = forms.EmailField(label='Email:', help_text=None, widget=forms.EmailInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'email@exemplu.ro'}),)

class PasswordResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(label='Noua parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'Noua parola'}),)
    new_password2 = forms.CharField(label='Confirmare parola noua:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Confirmare parola'}),)

class PasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'Parola actuala'}),)
    new_password1 = forms.CharField(label='Noua parola:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Noua parola'}),)
    new_password2 = forms.CharField(label='Confirmare parola noua:', help_text=None, strip=False, widget=forms.PasswordInput(attrs={'class': 'form-control', "autocomplete": "new-password", 'required': 'required', 'placeholder': 'Confirmare parola'}),)

class UserUpdateForm(forms.ModelForm):
    username = forms.CharField(label='User:', help_text=None, widget=forms.TextInput(attrs={'class': 'form-control', 'autofocus': 'autofocus', 'required': 'required', 'placeholder': 'Nume User'}),)
    class Meta:
        model = User
        fields = ['username']
 
class ProfilUpdateForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['nume', 'prenume', 'email', 'cnp', 'judet', 'oras', 'adresa', 'telefon', 'imagine']
        widgets = {
                 'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
                 'prenume': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
                 'email' : forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'email@exemplu.ro'}),
                 'cnp': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Nume'}),
                 'judet': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Judet'}),
                 'oras': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Oras'}),
                 'adresa': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Adresa'}),
                 'telefon': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Numar de telefon'}),
                 'imagine': forms.FileInput(attrs={'class': 'form-control'})
             }
