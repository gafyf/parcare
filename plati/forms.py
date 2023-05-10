from django import forms
from .models import Card
from django.utils.translation import gettext_lazy as _


class CardForm(forms.ModelForm):
    card_number = forms.CharField(label=_('Numar Card'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Numar Card')}))
    expiration_month = forms.CharField(label=_('Luna'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Luna')}))
    expiration_year = forms.CharField(label=_('An'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('An')}))
    cvc = forms.CharField(label=_('CVC'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('CVC')}))
    name = forms.CharField(label=_('Posesor Card'), widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': _('Posesor Card')}))

    class Meta:
        model = Card
        stripe_token = forms.CharField(widget=forms.HiddenInput)
        fields = ['name', 'card_number', 'expiration_month', 'expiration_year', 'cvc']
