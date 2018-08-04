from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

#from phonenumber_field.modelfields import PhoneNumberField
from .models import AllUser

class UserLoginForm(forms.Form):
    """Login form for both Members and Clients"""
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'login-form__username',
                                                                        'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'login-form__password',
                                                                            'placeholder': 'Password'}))

    class Meta:
        model = AllUser
        fields = ['username', 'password']

class UserRegisterForm(forms.Form):
    
    first_name = forms.CharField(label="", 
                                max_length=30, 
                                widget=forms.TextInput(attrs={'class':'register-form__first-name', 
                                        'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", 
                                max_length=30,
                                widget=forms.TextInput(attrs={'class':'register-form__last-name', 
                                        'placeholder': 'Last Name'}))
    username = forms.CharField(label="", 
                                max_length=30,
                                widget=forms.TextInput(attrs={'class':'register-form__username', 
                                        'placeholder': 'Username'}))
    email = forms.EmailField(label="",
                                max_length=50,
                                widget=forms.TextInput(attrs={'class':'register-form__email', 
                                        'placeholder': 'Email'}))
    password1 = forms.CharField(label="", 
                                widget=forms.PasswordInput(attrs={'class':'register-form__password1', 
                                        'placeholder': 'Password'}))

    password2 = forms.CharField(label="", 
                                widget=forms.PasswordInput(attrs={'class':'register-form__password2', 
                                        'placeholder': 'Confirm Password'}))
    
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

