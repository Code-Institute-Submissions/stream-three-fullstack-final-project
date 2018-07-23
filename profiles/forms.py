from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Profile

## Form for adding Profile details to Users ##
class ProfileForm(forms.Form):
    company = forms.CharField(max_length=50)
    phone = PhoneNumberField(widget=forms.TextInput(),
                            label='Phone Number')
    address1 = forms.CharField(required=False)
    address2 = forms.CharField(required=False)
    city = forms.CharField(required=False, label='City/Town')
    region = forms.CharField(required=False, label='Region/County')
    post_code = forms.CharField(required=False, label='Post Code')
    position = forms.CharField(max_length=50)

    #class Meta:
       # model = Profile
       # fields = ['company',
                   ## 'position', 
                   # 'phone',
                    #'address1',
                   ## 'address2',
                    #'address3',
                    #'post_code',
                    #]