from django import forms
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from .models import Profile

## Form for adding Profile details to Users ##
class ProfileForm(forms.Form):
    company = forms.CharField(max_length=50)
    position = forms.CharField(max_length=50)
    phone = PhoneNumberField(widget=forms.TextInput(),
                            label='Phone Number')
    address1 = forms.CharField()
    address2 = forms.CharField()
    city = forms.CharField(label='City/Town')
    region = forms.CharField(label='Region/County')
    post_code = forms.CharField(label='Post Code')
    country = CountryField(blank_label='Select Country').formfield()
   