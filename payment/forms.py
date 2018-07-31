from .models import Order
from django.forms import ModelForm
from django import forms
from django_countries.fields import CountryField

class OrderForm(ModelForm):
    country = CountryField(blank_label='Select Country').formfield()
    class Meta:
        model = Order
        fields = ['name_on_card', 
                    'address1', 
                    'address2',
                    'city',
                    'region',
                    'post_code',
                    'country',
                    'phone']

class PaymentForm(forms.Form):
    credit_card_number = forms.CharField(label='Credit/Debit Card Number')
    cvv = forms.CharField(label='Security Code (CVV)')
    expiry_month = forms.ChoiceField(label='Month', widget=forms.SelectDateWidget)
    expiry_year = forms.ChoiceField(label='Year', widget=forms.SelectDateWidget)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


