from django.test import TestCase
from .forms import OrderForm, PaymentForm

class TestPaymentForms(TestCase):

    def test_order_form(self):
        order = OrderForm({'country': 'US',
                            'name_on_card': 'Test Payee',
                            'address1': 'address1',
                            'address2': 'address2',
                            'city': 'city',
                            'region': 'region',
                            'post_code': 'post code',
                            'phone': '+441234567890'})

        self.assertTrue(order.is_valid())

 