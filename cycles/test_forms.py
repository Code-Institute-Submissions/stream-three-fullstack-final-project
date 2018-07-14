from django.test import TestCase
from django.shortcuts import get_object_or_404
from .forms import CycleForm
from accounts.models import AllUser
from manageclient.models import MemberClient


class TestCycleForm(TestCase):
    
    def test_cycle_form_is_not_valid(self):
        AllUser.objects.create_user(first_name='testadmin',
                                    last_name='test',
                                    username='testadmin',
                                    email='testadmin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )
        user_id = AllUser.objects.get(username='testadmin').pk
        new_form = CycleForm(user_id)

        self.assertFalse(new_form.is_valid())
           
    def test_cycle_form_is_valid(self):
        member = AllUser.objects.create_user(first_name='testadmin',
                                    last_name='test',
                                    username='testadmin',
                                    email='testadmin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )
        client = AllUser.objects.create_user(first_name='testclient',
                                        last_name='testclient',
                                        username='testclient',
                                        email='testclient@email.com',
                                        password='password',
                                        is_member=False,
                                        is_client=True
                                        )

        member = get_object_or_404(AllUser, username=member)
        client = get_object_or_404(AllUser, username=client)
        entry = MemberClient(member=member, client=client)
        entry.save()

        
        user_id = AllUser.objects.get(username='testadmin').pk
        client = MemberClient.objects.filter(member=user_id)
        print(user_id)

        new_form = CycleForm(user_id, {'job_title':'testjob',
                            'location':'testlocation',
                            'description':'testdescription',
                            'clients':client})

        self.assertTrue(new_form.is_valid())
        