from django.shortcuts import render
from django.http import HttpResponse
from django import forms
from django.template import loader

# Create your views here.
def home(request):
    return render(request, 'home.html')
