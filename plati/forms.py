from django import forms
from .models import Card

class CardForm(forms.ModelForm):
    class Meta:
        model = Card
        stripe_token = forms.CharField(widget=forms.HiddenInput)
        fields = ['name', 'card_number', 'expiration_month', 'expiration_year', 'cvc']
        widgets = {
            'card_number': forms.TextInput(attrs={'class': 'form-control', 'id': 'card-number', 'placeholder': 'Numar Card'}),
            'expiration_month': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'MM'}),
            'expiration_year': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'YY'}),
            'cvc': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'CVC'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Posesor Card'}),
        }
