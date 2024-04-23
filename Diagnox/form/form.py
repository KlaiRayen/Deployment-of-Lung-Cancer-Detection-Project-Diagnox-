'''from django.forms import ModelForm
from . import models
from .models import Arbre
from django import forms

class ArbreForm(ModelForm):
    class Meta:
        model = Arbre
        fields = ('nom','date_vu','localisation')'''
# forms.py
from django import forms

class CancerPredictionForm(forms.Form):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]
    SMOKING_CHOICES = [(1, 'No'), (2, 'Yes')]
    BOOLEAN_CHOICES = [(1, 'No'), (2, 'Yes')]

    gender = forms.ChoiceField(label='Gender', choices=GENDER_CHOICES)
    age = forms.IntegerField(label='Age')
    smoking = forms.ChoiceField(label='Smoking', choices=SMOKING_CHOICES)
    yellow_fingers = forms.ChoiceField(label='Yellow Fingers', choices=BOOLEAN_CHOICES)
    anxiety = forms.ChoiceField(label='Anxiety', choices=BOOLEAN_CHOICES)
    peer_pressure = forms.ChoiceField(label='Peer Pressure', choices=BOOLEAN_CHOICES)
    chronic_disease = forms.ChoiceField(label='Chronic Disease', choices=BOOLEAN_CHOICES)
    fatigue = forms.ChoiceField(label='Fatigue', choices=BOOLEAN_CHOICES)
    allergy = forms.ChoiceField(label='Allergy', choices=BOOLEAN_CHOICES)
    wheezing = forms.ChoiceField(label='Wheezing', choices=BOOLEAN_CHOICES)
    alcohol = forms.ChoiceField(label='Alcohol', choices=BOOLEAN_CHOICES)
    coughing = forms.ChoiceField(label='Coughing', choices=BOOLEAN_CHOICES)
    shortness_of_breath = forms.ChoiceField(label='Shortness of Breath', choices=BOOLEAN_CHOICES)
    swallowing_difficulty = forms.ChoiceField(label='Swallowing Difficulty', choices=BOOLEAN_CHOICES)
    chest_pain = forms.ChoiceField(label='Chest Pain', choices=BOOLEAN_CHOICES)
    lung_cancer = forms.ChoiceField(label='Lung Cancer', choices=BOOLEAN_CHOICES)
