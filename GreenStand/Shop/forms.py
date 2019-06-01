from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . import models 

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=20, required=True, help_text='*')
    last_name = forms.CharField(max_length=20, required=True, help_text='*')
    email = forms.EmailField(max_length=50, required=True, help_text='*')
    phone = forms.CharField(max_length=15, required=True, help_text='*')
    address = forms.CharField(max_length=100, required=True, help_text='*')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone', 'address', 'password1', 'password2', )