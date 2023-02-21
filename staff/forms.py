from django import forms

FUNCTIE = (
        (None, 'Selecteaza functia'),
        ('paznic', 'paznic'),
        ('electrician', 'electrician'),
        ('casier', 'casier'),
        ('secretara', 'secretara'),
        ('director', 'director'),
    )


class StaffNouForm(forms.Form):
    prenume = forms.CharField(label='Prenume', max_length=100)
    nume = forms.CharField(label='Nume', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)

    cnp = forms.CharField(label='CNP', max_length=100)
    judet = forms.CharField(label='Judet', max_length=100)
    oras = forms.CharField(label='Oras', max_length=100)
    adresa = forms.CharField(label='Adresa', max_length=100)
    telefon = forms.CharField(label='Telefon', max_length=100)
    marca = forms.CharField(label='Marca', max_length=100)
    model = forms.CharField(label='Model', max_length=100)
    numar = forms.CharField(label='Numar', max_length=100)
    culoare = forms.CharField(label='Culoare', max_length=100)
    combustibil = forms.CharField(label='Combustibil', max_length=100)

    functie = forms.ChoiceField(label='Functie', choices=FUNCTIE)
