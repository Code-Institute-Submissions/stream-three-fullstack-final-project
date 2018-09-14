from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
import re
from .models import AllUser

## LOGIN FORM ##
class UserLoginForm(forms.Form):
    
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'class':'login-form__input',
                                                                        'placeholder': 'Username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'class':'login-form__input',
                                                                            'placeholder': 'Password'}))

    class Meta:
        model = AllUser
        fields = ['username', 'password']

## REGISTRATION FORM FOR MEMBERS, DOUBLES AS CLIENT CREATION FORM ##
class UserRegisterForm(forms.Form):
    
    first_name = forms.CharField(label="",
                                required=True,
                                max_length=30, 
                                widget=forms.TextInput(attrs={'class':'register-form__input', 
                                        'placeholder': 'First Name'}))
    last_name = forms.CharField(label="", 
                                max_length=30,
                                widget=forms.TextInput(attrs={'class':'register-form__input', 
                                        'placeholder': 'Last Name'}))
    username = forms.CharField(label="", 
                                max_length=30,
                                widget=forms.TextInput(attrs={'class':'register-form__input', 
                                        'placeholder': 'Username'}))
    email = forms.EmailField(label="",
                                max_length=50,
                                widget=forms.TextInput(attrs={'class':'register-form__input', 
                                        'placeholder': 'Email'}))
    password1 = forms.CharField(label="", 
                                widget=forms.PasswordInput(attrs={'class':'register-form__input', 
                                        'placeholder': 'Password'}))

    password2 = forms.CharField(label="", 
                                widget=forms.PasswordInput(attrs={'class':'register-form__input', 
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

## credit https://www.geeksforgeeks.org/python-program-check-string-contains-special-character/ ##
    def check_string(self, _string):
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')

        if(regex.search(_string) == None):
            return False
        else:
            return True

    def clean_first_name(self): 
        first_name = self.cleaned_data.get('first_name')
        check_first_name = self.check_string(first_name)

        if check_first_name:
            raise forms.ValidationError(u"Your first name can't contain special characters.")
        elif " " in first_name:
            raise forms.ValidationError(u"Your first name can't contain spaces.")
        
        return first_name.capitalize()

    def clean_last_name(self): 
        last_name = self.cleaned_data.get('last_name')
        check_last_name = self.check_string(last_name)

        if check_last_name:
            raise forms.ValidationError(u"Your last name can't contain special characters.")
        elif " " in last_name:
            raise forms.ValidationError(u"Your last name can't contain spaces.")

        return last_name.capitalize() 

    def clean_username(self):
        username = self.cleaned_data.get('username')
        check_username = self.check_string(username)

   
        if AllUser.objects.filter(username=username):
            raise forms.ValidationError(u'Username is already taken.')
        elif check_username:
            raise forms.ValidationError(u"Your username can't contain special characters.")
        elif " " in username:
            raise forms.ValidationError(u"Your username can't contain spaces.")
        
        return username
     
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if AllUser.objects.filter(email=email):
            raise forms.ValidationError(u'Email address is already taken.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
   
        if not password1 or not password2: 
            raise ValidationError("Please confirm your password.")

        if password1 != password2:
            raise ValidationError("Passwords must match!")

        return password1

