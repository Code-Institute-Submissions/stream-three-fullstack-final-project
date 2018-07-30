from .models import Payment
from django.forms import ModelForm
from django_countries.fields import CountryField

class PaymentForm(ModelForm):
    country = CountryField(blank_label='Select Country').formfield()
    class Meta:
        model = Payment
        fields = ['name_on_card', 
                    'address1', 
                    'address2',
                    'city',
                    'region',
                    'post_code',
                    'country',
                    'phone']
       