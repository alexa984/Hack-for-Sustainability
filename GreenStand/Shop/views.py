from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.template import loader
from django.core.exceptions import ValidationError
from datetime import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from . import models
from .forms import RegisterForm,FarmerRegisterForm,CustomerRegisterForm,LoginForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password

def home(request):
    return render(request, 'home.html')

def register_as(request):
    return render(request, 'register_as.html')

def register(request, user_type):
    template = 'register.html'
    if request.method == 'POST':
        if user_type == 'customer':
            form = CustomerRegisterForm(request.POST)
            user_class = models.Customer
        elif user_type == 'farmer':
            form = FarmerRegisterForm(request.POST)
            user_class = models.Farmer
        if form.is_valid():
            if models.Customer.objects.filter(username=form.cleaned_data['username']).exists() or models.Farmer.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif user_class.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password'] != form.cleaned_data['confirm_password']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                user = user_class.objects.create(
                    username=form.cleaned_data['username'],
                    password=make_password(form.cleaned_data['password'],salt='sha1-7',hasher='pbkdf2_sha256'),
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    phone=form.cleaned_data['phone'],
                    email=form.cleaned_data['email'],
                )
                if user_type =='farmer':
                    user.certification_number = form.cleaned_data['certification_number']
                    user.save()
                
                return redirect('home')
            
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})

def login(request):
    template = 'login.html'
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def add_item(request):
    pass

def authorize(request):
    return render(request, 'authorize.html')
