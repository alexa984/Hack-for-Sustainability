from django import forms
from django.forms import ModelForm
from . import models

class RegisterForm(ModelForm):
    username = forms.CharField(max_length=50, required=True, help_text='*')
    password = forms.CharField(label=("Password"), widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text='*')
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}),help_text='*')
    first_name = forms.CharField(max_length=20, required=True, help_text='*')
    last_name = forms.CharField(max_length=20, required=True, help_text='*')
    email = forms.EmailField(max_length=50, required=True, help_text='*',
        widget=forms.EmailInput(attrs={'class':'form-control'}))
    phone = forms.CharField(max_length=15, required=True, help_text='*')
    address = forms.CharField(max_length=100, required=True, help_text='*')
    is_farmer = forms.BooleanField(default=False)

    class Meta:
        model = models.Account
        fields = ('username',  'password', 'confirm_password', 'first_name', 'last_name', 'email', 'phone', 'address', 'is_farmer')