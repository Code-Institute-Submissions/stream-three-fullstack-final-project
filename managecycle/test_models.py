from django.test import TestCase
from .models import Cycles
from accounts.models import AllUser

## CYCLE MODEL TEST ##
class TestCyclesModel(TestCase):
    
    def setUp(self):
        self.create_member = AllUser.objects.create_user(first_name='testadmin',
                                        last_name='test',
                                        username='testadmin',
                                        email='testadmin1@email.com',
                                        password='password',
                                        is_member=True,
                                        is_client=False
                                        )
        self.create_client = AllUser.objects.create_user(first_name='testclient',
                                        last_name='test',
                                        username='testclient',
                                        email='testclient@email.com',
                                        password='password',
                                        is_member=False,
                                        is_client=True
                                        )
        
    def test_create_a_cycle(self):
        
        job_title = 'Test Job'
        location = 'Test Location'
        description = 'Description'
        member = AllUser.objects.get(username='testadmin')
        client = AllUser.objects.get(username='testclient')

        new_cycle = Cycles(job_title=job_title,
                            location=location,
                            description=description,
                            member=member,
                            client=client)
        new_cycle.save()
        get_cycle=Cycles.objects.get(member=member)

        self.assertEqual(get_cycle.member, member)
        self.assertEqual(get_cycle.client, client)