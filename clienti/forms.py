from django import forms
from .models import Masina
from django.utils.translation import gettext_lazy as _


TIP = (
        (None, _('Alege contract')),
        ('public (500Lei)', _('public (500Lei)')),
        ('privat (800Lei)', _('privat (800Lei)')),
    )


class ClientNouForm(forms.Form):
    nume = forms.CharField(label=_('Nume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nume')}))
    prenume = forms.CharField(label=_('Prenume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Prenume')}))
    email = forms.EmailField(label=_('Email'), widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': _('Email')}))
    cnp = forms.CharField(label=_('CNP'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('CNP')}))
    judet = forms.CharField(label=_('Judet'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Judet')}))
    oras = forms.CharField(label=_('Oras'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Oras')}))
    adresa = forms.CharField(label=_('Adresa'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Adresa')}))
    telefon = forms.CharField(label=_('Telefon'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telefon')}))
    nr_permis = forms.CharField(label=_('Numar Permis Auto'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Numar Permis Auto')}))
    categ_permis = forms.CharField(label=_('Categorie Permis Auto'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Categorie Permis Auto')}))
    marca = forms.CharField(label=_('Marca'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Marca')}))
    model = forms.CharField(label=_('Model'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Model')}))
    numar = forms.CharField(label=_('Numar'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Numar'), 'required': 'required'}))
    culoare = forms.CharField(label=_('Culoare'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Culoare')}))
    combustibil = forms.CharField(label=_('Combustibil'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Combustibil')}))
    contract = forms.ChoiceField(label=_('Contract'), choices=TIP, widget=forms.Select(attrs={'class': 'form-control'}))


class MasinaForm(forms.ModelForm):
    marca = forms.CharField(label=_('Marca'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Marca')}))
    model = forms.CharField(label=_('Model'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Model')}))
    numar = forms.CharField(label=_('Numar'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Numar'), 'required': 'required'}))
    culoare = forms.CharField(label=_('Culoare'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Culoare')}))
    combustibil = forms.CharField(label=_('Combustibil'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Combustibil')}))

    class Meta:
        model = Masina
        fields = ['marca', 'model', 'numar', 'culoare', 'combustibil']
        exclude = ['profil']
