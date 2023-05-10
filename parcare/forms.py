from django import forms
from .models import Imagine
from django.utils.translation import gettext as _


class ImagineForm(forms.ModelForm):
    nume = forms.CharField(label=_('Nume Imagine'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Descriere Imagine')}))
    imagine = forms.FileField(label=_('Imagine'), widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': _('Adauga Imagine')}))

    class Meta:
        model = Imagine
        fields = ['nume', 'imagine']
