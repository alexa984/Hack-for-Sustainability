from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
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

    class Meta:
        model = User
        fields = ('username',  'password', 'confirm_password', 'first_name', 'last_name', 'email', 'phone', 'address')


class CustomerRegisterForm(RegisterForm):
    pass
    # class Meta:
    #     model = models.Customer
    #     fields = ('username',  'password', 'confirm_password', 'first_name', 'last_name', 'email', 'phone', 'address')

class FarmerRegisterForm(RegisterForm):
    certification_number = forms.CharField(max_length=80,required=True,help_text='*')

    class Meta(RegisterForm.Meta):
        model = User
        fields = RegisterForm.Meta.fields + ('certification_number',)

class LoginForm(AuthenticationForm):

    class Meta:
        model = User
        fields = ('username', 'password')