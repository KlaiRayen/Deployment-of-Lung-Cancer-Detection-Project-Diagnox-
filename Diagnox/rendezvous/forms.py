from django import forms
from .models import Rendezvous

class RendezvousForm(forms.ModelForm):
    class Meta:
        model = Rendezvous
        fields = ['date', 'note']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
        }
