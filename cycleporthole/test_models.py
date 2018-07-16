from django.test import TestCase
from .models import Quotes, PurchaseOrder, Invoices
from accounts.models import AllUser
from cycles.models import Cycles
from djmoney.money import Money

class TestCyclePortholeModels(TestCase):
    
    def test_quotes_model(self):
        create_member = AllUser.objects.create_user(first_name='test1admin',
                                    last_name='test1',
                                    username='test1admin',
                                    email='test1admin1@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )
        create_client = AllUser.objects.create_user(first_name='test1client',
                                        last_name='test1',
                                        username='test1client',
                                        email='test1client@email.com',
                                        password='password',
                                        is_member=False,
                                        is_client=True
                                        ) 
        cycle_value = [('1.00', 'GBP')]
        member = AllUser.objects.get(username='test1admin')
        client = AllUser.objects.get(username='test1client')
        new_cycle = Cycles(job_title='job_title',
                            location='location',
                            description='description',
                            member=member,
                            client=client)
        new_cycle.save()
        cycle = Cycles.objects.get(job_title='job_title')
        new_quote = Quotes(cycle_value=Money(1,'GBP'),
                            client=client,
                            member=member,
                            cycle=cycle,
                            is_quote=True)

        new_quote.save()
        quote = Quotes.objects.get(member=member)

        self.assertEqual(member.username, quote.member.username)
