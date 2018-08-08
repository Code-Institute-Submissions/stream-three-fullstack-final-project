from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from .models import Profile

## Form for adding Profile details to Users ##
class ProfileForm(forms.Form):
    company = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'Company',
                                        'class':'profile-form__input'})
                                )
    position = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'Position',
                                'class':'profile-form__input'}))
    phone = PhoneNumberField(label="",
                            widget=forms.TextInput(
                            attrs={'placeholder':'Phone Number inc Country Code',
                            'class':'profile-form__input'})
                            )
    address1 = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'House/Flat No.',
                                    'class':'profile-form__input'})
                                )
    address2 = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'Street',
                                    'class':'profile-form__input'})
                                )
    city = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'City',
                                    'class':'profile-form__input'}))
    region = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'Region',
                                    'class':'profile-form__input'}))
    post_code = forms.CharField(max_length=50,
                                label="",
                                widget=forms.TextInput(
                                attrs={'placeholder':'Post Code',
                                    'class':'profile-form__input'}))
    country = CountryField(blank_label='Select Country').formfield(label="")
   