'''from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .form import ArbreForm
from .models import Arbre
from .import models
from django import forms

# Create your views here.


def index(request):
    if request.method == "POST": 
        form = ArbreForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = ArbreForm()
        
    return render(request, "form.html", {'form':form})'''
# views.py
from django.shortcuts import render
from .form import CancerPredictionForm

def index(request):
    if request.method == 'POST':
        form = CancerPredictionForm(request.POST)
        if form.is_valid():
            
            return render(request, 'success.html')
    else:
        form = CancerPredictionForm()
    return render(request, 'form.html', {'form': form})



