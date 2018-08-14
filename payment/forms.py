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
    MONTHS = [(1,'January'),
               (2, 'February'),
               (3, 'March'),
               (4, 'April'),
               (5, 'May'),
               (6, 'June'),
               (7, 'July'),
               (8, 'August'),
               (9, 'September'),
               (10, 'October'),
               (11, 'November'),
               (12, 'December')]

    YEARS = [(i,i) for i in range (2018, 2051)]
    credit_card_number = forms.CharField(label='Credit/Debit Card Number', required=False)
    cvv = forms.CharField(label='Security Code (CVV)', required=False)
    expiry_month = forms.ChoiceField(label='Expiry Month', choices=MONTHS, required=False)
    expiry_year = forms.ChoiceField(label='Expiry Year', choices=YEARS, required=False)
    stripe_id = forms.CharField(widget=forms.HiddenInput)


