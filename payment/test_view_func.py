from django.test import TestCase, RequestFactory
from fileo.testing_models import CreateTestModels
from .view_func import convert_total_for_stripe, save_order, set_status_to_complete
from .forms import OrderForm
from .models import Payment

class TestPaymentViewHelpers(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.job = self.models.create_job()
        self.cycle = self.models.create_cycle()
        self.order = {'country': 'US',
                        'name_on_card': 'Test Payee',
                        'address1': 'address1',
                        'address2': 'address2',
                        'city': 'city',
                        'region': 'region',
                        'post_code': 'post code',
                        'phone': '+441234567890'}

    def test_convert_total_for_stripe(self):
        total = '123,213.00 GBP'
        converted = convert_total_for_stripe(total)

        self.assertEqual(converted, 12321300)

    def test_save_order(self):
        order_form = OrderForm(self.order)
        if order_form.is_valid():
            order = save_order(self.cycle, order_form)
        
        saved_order = Payment.objects.get(name_on_card=self.order['name_on_card'])
        self.assertTrue(saved_order)
        self.assertEqual(saved_order.name_on_card, self.order['name_on_card'])

    def test_set_status_to_complete(self):
        set_status = set_status_to_complete(self.cycle)
        status = self.models.get_cycle_status()

        self.assertTrue(status.complete)
        self.assertFalse(status.pending)
        self.assertFalse(status.cancelled)