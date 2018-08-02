from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#from phonenumber_field.modelfields import PhoneNumberField
from .models import AllUser

class UserLoginForm(forms.Form):
    """Login form for both Members and Clients"""
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'login-form__username',
                                                                        'placeholder': 'Email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'login-form__password',
                                                                            'placeholder': 'Password'}))

    class Meta:
        model = AllUser
        fields = ['username', 'password']

class UserRegisterForm(forms.Form):
    
    first_name = forms.CharField(label='First Name',max_length=30)
    last_name = forms.CharField(label='Last Name', max_length=30)
    username = forms.CharField(label='Username', max_length=30)
    email = forms.EmailField(max_length=254)
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    class Meta:
        model = AllUser
        fields = [
                    'first_name', 
                    'last_name',
                    'username',
                    'email',
                    'password1',
                    'password2',
                 ]

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if AllUser.objects.filter(username=username):
            raise forms.ValidationError(u'Username is already taken.')
        return username
     
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if AllUser.objects.filter(email=email):
            raise forms.ValidationError(u'Email address is already taken.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
   
        if not password1 or not password2: # if there is no value for pword1 or pword2
            raise ValidationError("Please confirm your password.") # Raise an error

        if password1 != password2:
            raise ValidationError("Passwords must match!")

        return password1

