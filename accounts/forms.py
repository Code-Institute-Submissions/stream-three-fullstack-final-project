from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from .models import AllUser

class UserLoginForm(forms.Form):
    """Login form for both Members and Clients"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'login__form-username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login__form-password'}))

    class Meta:
        model = AllUser
        fields = ['username', 'password']

class UserSignUpForm(UserCreationForm):
    
    
    class Meta:
        model = AllUser
        fields = ('username',
                    'first_name', 
                    'last_name',
                    'company',
                    'phone',
                    'postion',
                    'email',
                    'password1',
                    'password2',
                 )
