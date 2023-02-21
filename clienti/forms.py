from django import forms
from .models import Masina

TIP = (
        (None, 'Selecteaza contract'),
        ('public', 'public'),
        ('privat', 'privat')
    )

class ClientNouForm(forms.Form):
    nume = forms.CharField(label='Nume', max_length=100)
    prenume = forms.CharField(label='Prenume', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    cnp = forms.CharField(label='CNP', max_length=100)
    judet = forms.CharField(label='Judet', max_length=100)
    oras = forms.CharField(label='Oras', max_length=100)
    adresa = forms.CharField(label='Adresa', max_length=100)
    telefon = forms.CharField(label='Telefon', max_length=100)
    nr_permis = forms.CharField(label='Numar Permis Auto', max_length=100)
    categ_permis = forms.CharField(label='Categorie Permis Auto', max_length=100)
    marca = forms.CharField(label='Marca', max_length=100)
    model = forms.CharField(label='Model', max_length=100)
    numar = forms.CharField(label='Numar', max_length=100)
    culoare = forms.CharField(label='Culoare', max_length=100)
    combustibil = forms.CharField(label='Combustibil', max_length=100)
    contract = forms.ChoiceField(label='Contract', choices=TIP)


class MasinaForm(forms.ModelForm):
    class Meta:
        model = Masina
        fields = ['marca', 'model', 'numar', 'culoare', 'combustibil']
        exlude = ['profil']
        widgets = {
                 'marca': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Marca'}),
                 'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Model'}),
                 'numar': forms.TextInput(attrs={'class': 'form-control', 'required': 'required', 'placeholder': 'Numar'}),
                 'culoare': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Culoare'}),
                 'combustibil': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Combustibil'})
                }
        