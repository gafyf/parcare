from django import forms
from .models import Imagine


class ImagineForm(forms.ModelForm):
    class Meta:
        model = Imagine
        fields = ['nume', 'imagine']
        widgets = {
                 'nume': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Descriere Imagine'}),
                 'imagine': forms.FileInput(attrs={'class': 'form-control'})
             }

