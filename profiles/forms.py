from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

class ProfileForm(forms.Form):
    company = forms.CharField(max_length=50)
    phone = PhoneNumberField(widget=forms.TextInput(),
                            label='Phone Number', 
                            required=False)
    position = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Profile
        fields = ['company', 'phone', 'position']