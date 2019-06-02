from django.shortcuts import render
from django.http import HttpResponse
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
from .forms import CustomerRegisterForm, LoginForm


def home(request):
    return render(request, 'home.html')

def customer_register(request):
    template = 'register.html'
    if request.method == 'POST':
        form = CustomerRegisterForm(request.POST)
        if form.is_valid():
            if models.Customer.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif models.Customer.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                customer = models.Customer.objects.create(
                    username=form.cleaned_data['username'],
                    password=form.cleaned_data['password1'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'],
                    address=form.cleaned_data['address'],
                    phone=form.cleaned_data['phone'],
                    email=form.cleaned_data['email'],
                )
                # user.first_name = form.cleaned_data['first_name']
                # user.last_name = form.cleaned_data['last_name']
                # user.phone_number = form.cleaned_data['phone_number']
                # user.save()
               
                # Login the user
                # login(request, customer)
               
                # redirect to accounts page:
                return redirect('home')
            # form.save()
            # username = form.cleaned_data.get('username')
            # raw_password = form.cleaned_data.get('password')
            # user = authenticate(username=username, password=raw_password)
            # login(request, user)
            # return redirect('home')
    else:
        form = CustomerRegisterForm()
    return render(request, 'register.html', {'form': form})

# def user_login(request):
#     if request.method == 'POST':
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('home')
#     else:
#         form = LoginForm()
#     return render(request, 'login.html', {'form': form})
