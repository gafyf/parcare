from django import forms
from django.utils.translation import gettext_lazy as _

FUNCTIE = (
        (None, _('Selecteaza functia')),
        ('paznic', _('paznic')),
        ('electrician', _('electrician')),
        ('casier', _('casier')),
        ('secretara', _('secretara')),
        ('director', _('director')),
    )

class StaffNouForm(forms.Form):
    prenume = forms.CharField(label=_('Prenume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Prenume')}))
    nume = forms.CharField(label=_('Nume'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Nume')}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': _('email@exemplu.ro')}))

    cnp = forms.CharField(label=_('CNP'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('CNP')}))
    judet = forms.CharField(label=_('Judet'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Judet')}))
    oras = forms.CharField(label=_('Oras'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Oras')}))
    adresa = forms.CharField(label=_('Adresa'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Adresa')}))
    telefon = forms.CharField(label=_('Telefon'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Telefon')}))
    marca = forms.CharField(label=_('Marca'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Marca')}))
    model = forms.CharField(label=_('Model'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Model')}))
    numar = forms.CharField(label=_('Numar'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Numar'), 'required': 'required'}))
    culoare = forms.CharField(label=_('Culoare'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Culoare')}))
    combustibil = forms.CharField(label=_('Combustibil'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Combustibil')}))

    functie = forms.ChoiceField(label=_('Functie'), choices=FUNCTIE, widget=forms.Select(attrs={'class': 'form-control'}))

