from django import forms
from .models import Profile

class ProfileForm(forms.Form):
    
    company = forms.CharField(max_length=50)
    phone = forms.CharField(max_length=50, required=False)
    position = forms.CharField(max_length=50, required=False)

    class Meta:
        model = Profile
        fields = ['company', 'phone', 'position']