from django.test import TestCase
from django.db import models
from django.dispatch import Signal, receiver
from unittest import mock
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from cycles.models import Cycles
from djmoney.money import Money

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

## 
class TestCyclePortholeSignalIsSentOnDelete(TestCase):

    def setUp(self):
        AllUser.objects.create_user(first_name='test1admin',
                                last_name='test1',
                                username='test1admin',
                                email='test1admin1@email.com',
                                password='password',
                                is_member=True,
                                is_client=False
                                )
        AllUser.objects.create_user(first_name='test1client',
                                    last_name='test1',
                                    username='test1client',
                                    email='test1client@email.com',
                                    password='password',
                                    is_member=False,
                                    is_client=True
                                    )
        new_cycle = Cycles(job_title='job_title',
                            location='location',
                            description='description',
                            member=AllUser.objects.get(username='test1admin'),
                            client=AllUser.objects.get(username='test1client'))
        new_cycle.save()

        self.member = AllUser.objects.get(username='test1admin')
        self.client = AllUser.objects.get(username='test1client')
        self.cycle = Cycles.objects.get(job_title='job_title')


    def test_signal_sent_when_quote_deleted(self):
        new_quote = Quotes(cycle_value=Money(1,'GBP'),
                            client=self.client,
                            member=self.member,
                            cycle=self.cycle,
                            is_quote=True)
        new_quote.save()
        quote = Quotes.objects.get(member=self.member)

        with CatchSignal(models.signals.post_delete) as handler:
            quote.delete()

        handler.assert_called()

    def test_signal_sent_when_po_deleted(self):
        new_po = PurchaseOrder(client=self.client,
                                member=self.member,
                                cycle=self.cycle,
                                is_po=True)
        new_po.save()
        po = PurchaseOrder.objects.get(member=self.member)

        with CatchSignal(models.signals.post_delete) as handler:
            po.delete()

        handler.assert_called()

    def test_signal_sent_when_invoice_deleted(self):
        new_invoice = Invoices(client=self.client,
                                member=self.member,
                                cycle=self.cycle,
                                is_invoice=True)
        new_invoice.save()
        invoice = Invoices.objects.get(member=self.member)

        with CatchSignal(models.signals.post_delete) as handler:
            invoice.delete()

        handler.assert_called()