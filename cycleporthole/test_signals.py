from django.test import TestCase
from django.db import models
from django.dispatch import Signal, receiver
from unittest import mock
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from managecycle.models import Cycles
from djmoney.money import Money
#from .signals import 

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
        
        self.member = AllUser.objects.get(username='test1admin')
        self.client = AllUser.objects.get(username='test1client')
        self.cycle = Cycles.objects.get(cycle_title='cycle_title')
        new_job = Jobs(job_title='test job',
                        job_number='1',
                        member=self.member,
                        client=self.client)
        new_job.save()
        new_cycle = Cycles(cycle_title='cycle_title',
                            description='description',
                            location='location',
                            start_date='2018-01-01',
                            end_date='2018-01-01',
                            member=member,
                            client=client,
                            job=Jobs.objects.get(member=member))
        new_cycle.save()

    def test_signal_sent_when_quote_deleted(self):
        new_quote = Quotes(client=self.client,
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