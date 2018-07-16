from django.test import TestCase
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from cycles.models import Cycles
from djmoney.money import Money

## Test Helper Functions ##
def create_cycle(member, client):
    new_cycle = Cycles(job_title='job_title',
                        location='location',
                        description='description',
                        member=member,
                        client=client)
    new_cycle.save()

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
        new_cycle = Cycles(job_title='job_title',
                            location='location',
                            description='description',
                            member=AllUser.objects.get(username='test1admin'),
                            client=AllUser.objects.get(username='test1client'))
        new_cycle.save()

    def test_quotes_model(self):

        member = AllUser.objects.get(username='test1admin')
        client = AllUser.objects.get(username='test1client')
        #create_cycle(self.member, self.client)
        cycle = Cycles.objects.get(job_title='job_title')
        new_quote = Quotes(cycle_value=Money(1,'GBP'),
                            client=client,
                            member=member,
                            cycle=cycle,
                            is_quote=True)
        new_quote.save()

        quote = Quotes.objects.get(member=member)

        self.assertEqual(member.username, quote.member.username)
        self.assertEqual(client.username, quote.client.username)
        self.assertEqual(cycle.job_title, quote.cycle.job_title)
        self.assertTrue(quote.is_quote)
        self.assertEqual(quote.cycle_value, Money(1,'GBP'))

    def test_po_model(self):
        member = AllUser.objects.get(username='test1admin')
        client = AllUser.objects.get(username='test1client')
        #create_cycle(member, client)
        cycle = Cycles.objects.get(job_title='job_title')
        new_po = PurchaseOrder(client=client,
                        member=member,
                        cycle=cycle,
                        is_po=True)

        new_po.save()

        po = PurchaseOrder.objects.get(member=member)

        self.assertEqual(member.username, po.member.username)
        self.assertEqual(client.username, po.client.username)
        self.assertEqual(cycle.job_title, po.cycle.job_title)
        self.assertTrue(po.is_po)

    def test_invoice_model(self):
        member = AllUser.objects.get(username='test1admin')
        client = AllUser.objects.get(username='test1client')
        #create_cycle(member, client)
        cycle = Cycles.objects.get(job_title='job_title')
        
        new_invoice = Invoices(client=client,
                        member=member,
                        cycle=cycle,
                        is_invoice=True)

        new_invoice.save()

        invoice = Invoices.objects.get(member=member)

        self.assertEqual(member.username, invoice.member.username)
        self.assertEqual(client.username, invoice.client.username)
        self.assertEqual(cycle.job_title, invoice.cycle.job_title)
        self.assertTrue(invoice.is_invoice)
            
