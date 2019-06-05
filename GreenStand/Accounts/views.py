from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.template import loader
from django.views import View
from django.shortcuts import render, redirect
from . import models
from .forms import RegisterForm
from django.contrib.auth.hashers import PBKDF2PasswordHasher, make_password

def login(request):
        #give a form to the template
        return render(request, 'login.html')

def register_as(request):
        return render(request, 'register_as.html')

def register(request, user_type):
    template = 'register.html'
    is_farmer_bool = False
    if user_type=='farmer':
        is_farmer_bool=True

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if models.Account.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif models.Account.objects.filter(email=form.cleaned_data['email']).exists():
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
                account = Account.objects.create(
                    username=form.cleaned_data['username'],
                    password=make_password(form.cleaned_data['password'],salt='sha1-7',hasher='pbkdf2_sha256'),
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    phone=form.cleaned_data['phone'],
                    email=form.cleaned_data['email'],
                    is_farmer=is_farmer_bool
                )
                return redirect('localhost:8000/')
    else:
        form = RegisterForm()
    return render(request, template, {'form': form})