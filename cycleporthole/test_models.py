import datetime
from django.test import TestCase
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from managecycle.models import Cycles
from managejobs.models import Jobs
from djmoney.money import Money



class TestCyclePortholeModels(TestCase):
    
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
        member=AllUser.objects.get(username='test1admin')
        client=AllUser.objects.get(username='test1client')

        new_job = Jobs(job_title='test job',
                        job_number='1',
                        member=member,
                        client=client)
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

        self.member = AllUser.objects.get(username='test1admin')
        self.client = AllUser.objects.get(username='test1client')
        self.cycle = Cycles.objects.get(cycle_title='cycle_title')

    def test_quotes_model(self):
        new_quote = Quotes(cycle_value=Money(1,'GBP'),
                            uploaded_at=datetime.datetime.now(),
                            client=self.client,
                            member=self.member,
                            cycle=self.cycle,
                            is_quote=True)
        new_quote.save()

        quote = Quotes.objects.get(member=self.member)

        self.assertEqual(self.member.username, quote.member.username)
        self.assertEqual(self.client.username, quote.client.username)
        self.assertEqual(self.cycle.cycle_title, quote.cycle.cycle_title)
        self.assertTrue(quote.is_quote)
        self.assertEqual(quote.cycle_value, Money(1,'GBP'))

    def test_po_model(self):
        new_po = PurchaseOrder(client=self.client,
                        uploaded_at=datetime.datetime.now(),
                        member=self.member,
                        cycle=self.cycle,
                        is_po=True)

        new_po.save()
        po = PurchaseOrder.objects.get(member=self.member)

        self.assertEqual(self.member.username, po.member.username)
        self.assertEqual(self.client.username, po.client.username)
        self.assertEqual(self.cycle.cycle_title, po.cycle.cycle_title)
        self.assertTrue(po.is_po)

    def test_invoice_model(self):
        new_invoice = Invoices(client=self.client,
                        uploaded_at=datetime.datetime.now(),        
                        member=self.member,
                        cycle=self.cycle,
                        is_invoice=True)

        new_invoice.save()
        invoice = Invoices.objects.get(member=self.member)

        self.assertEqual(self.member.username, invoice.member.username)
        self.assertEqual(self.client.username, invoice.client.username)
        self.assertEqual(self.cycle.cycle_title, invoice.cycle.cycle_title)
        self.assertTrue(invoice.is_invoice)
            
