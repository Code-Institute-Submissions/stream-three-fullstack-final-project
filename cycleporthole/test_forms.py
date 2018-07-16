from django.test import TestCase
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from djmoney.money import Money

class TestCyclePortholeForms(TestCase):

    def test_quotes_form(self):
        form = {'file': 'quotes',
                'cycle_value': Money(1, 'GBP')}