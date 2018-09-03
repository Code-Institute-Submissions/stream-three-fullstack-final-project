from django.test import TestCase
from django.db import models
from django.dispatch import Signal, receiver
from unittest import mock
from .models import CycleStatus
from .signals import reset_quote_status, reset_po_status, reset_invoice_status
from cycleporthole.test_signals import CatchSignal
from accounts.models import AllUser
from fileo.testing_models import CreateTestModels


## TEST SIGNALS ARE RECEIVED AND STATUSES RESET ##
## WHEN A NEW FILE IS UPLOADED ##
class TestResetStatusOnSignal(TestCase):

    def setUp(self):
        self.new_models = CreateTestModels()
        self.job = self.new_models.create_job()
        self.cycle = self.new_models.create_cycle()
        self.status = self.new_models.get_cycle_status()
        self.new_models.create_quote()
        self.new_models.create_po()
        self.new_models.create_invoice()
        self.quote = self.new_models.get_quote()
        self.po = self.new_models.get_po()
        self.invoice = self.new_models.get_invoice()
       
    
    def test_reset_quote_status(self):
        self.status.approve_quote = True
        self.status.contest_quote = True
        self.status.save(update_fields=['approve_quote',
                                    'contest_quote'])

        reset = reset_quote_status(self.quote)

        self.assertFalse(reset.approve_quote)
        self.assertFalse(reset.contest_quote)

    def test_reset_po_status(self):
        self.status.approve_po = True
        self.status.contest_po = True
        self.status.save(update_fields=['approve_po',
                                    'contest_po'])

        reset = reset_po_status(self.po)
        
        self.assertFalse(reset.approve_po)
       
    def test_reset_invoice_status(self):
        self.status.approve_invoice = True
        self.status.contest_invoice = True
        self.status.save(update_fields=['approve_invoice',
                                    'contest_invoice'])

        reset = reset_invoice_status(self.invoice)
        
        self.assertFalse(reset.approve_invoice)
    
    def test_set_default_status_signal_sent_on_cycle_save(self):
        with CatchSignal(models.signals.post_save) as handler:
            cycle = self.new_models.get_cycle()
            cycle.save()
        
        handler.assert_called()

    def test_signal_recieved_on_quote_save(self):
        with CatchSignal(models.signals.post_save) as handler:
            self.quote.save()
        
        handler.assert_called()

    def test_signal_recieved_on_po_save(self):
        with CatchSignal(models.signals.post_save) as handler:
            self.po.save()
    
        handler.assert_called()

    def test_signal_received_on_invoice_save(self):
        with CatchSignal(models.signals.post_save) as handler:
            self.invoice.save()
    
        handler.assert_called()