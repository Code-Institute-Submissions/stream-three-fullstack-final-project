from django.test import TestCase
from django.db import models
from django.dispatch import Signal, receiver
from unittest import mock
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from managecycle.models import Cycles
from djmoney.money import Money
from fileo.testing_models import CreateTestModels


## Catch Signal Class ##
class CatchSignal:
    def __init__(self, signal):
        self.signal = signal
        self.handler = mock.Mock()

    def __enter__(self):
        self.signal.connect(self.handler)
        return self.handler
    
    def __exit__(self, exc_type, exc_value, tb):
        self.signal.disconnect(self.handler)


class TestCyclePortholeSignalIsSentOnDelete(TestCase):

    ## Build Model Objects ##
    def setUp(self):
        new_models = CreateTestModels()
        new_models.create_job()
        new_models.create_cycle()
        new_models.create_quote()
        new_models.create_po()
        new_models.create_invoice()
        self.quote = new_models.get_quote()
        self.po = new_models.get_po()
        self.invoice = new_models.get_invoice()

   # def test_signal_sent_when_quote_deleted(self):
    #    quote = self.quote
#
 #       with CatchSignal(models.signals.post_delete) as handler:
  #          quote.delete()

   #     handler.assert_called()

    #def test_signal_sent_when_po_deleted(self):

     #   po = self.po
      #  with CatchSignal(models.signals.post_delete) as handler:
       #     po.delete()

        #handler.assert_called()

    #def test_signal_sent_when_invoice_deleted(self):
     #   invoice = self.invoice
      #  with CatchSignal(models.signals.post_delete) as handler:
       #     invoice.delete()

      #  handler.assert_called()