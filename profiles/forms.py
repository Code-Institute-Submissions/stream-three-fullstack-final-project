from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

## Form for adding Profile details to Users ##
class ProfileForm(forms.Form):
    company = forms.CharField(max_length=50)
    phone = PhoneNumberField(widget=forms.TextInput(),
                            label='Phone Number')
    position = forms.CharField(max_length=50)

    class Meta:
        model = Profile
        fields = ['company', 'phone', 'position']