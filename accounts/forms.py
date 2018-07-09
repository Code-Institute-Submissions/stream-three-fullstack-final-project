from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
#from phonenumber_field.modelfields import PhoneNumberField
from .models import AllUser

class UserLoginForm(forms.Form):
    """Login form for both Members and Clients"""
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'login__form-username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'login__form-password'}))

    class Meta:
        model = AllUser
        fields = ['username', 'password']

class UserRegisterForm(forms.Form):
    
    
    first_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    company = forms.CharField(label='Company Name', required=False, max_length=50)
    phone = forms.IntegerField(widget=forms.TextInput(attrs={'type': 'number'}), 
                            label='Phone', required=False)
    #phone = PhoneNumberField()
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(label='Password1', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password2', widget=forms.PasswordInput)
    
    class Meta:
        model = AllUser
        fields = [
                    'first_name', 
                    'last_name',
                    'company',
                    'phone',
                    'postion',
                    'username',
                    'email',
                    'password1',
                    'password2',
                 ]

    def check_email(self):
        email = self.cleaned_data.get('email')

        if AllUser.objects.get(email=email):
            raise forms.ValidationError(u'Email address is already taken.')
        return email

    def check_password(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password1 or not password2:
            raise forms.ValidationError('Please enter your passwords.')
        
        if password1 != password2:
            raise forms.ValidationError('Please check your passwords are matching.')

        return password1

