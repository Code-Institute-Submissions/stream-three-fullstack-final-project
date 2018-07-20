from django.test import TestCase
from django.shortcuts import get_object_or_404
from .forms import CycleForm
from accounts.models import AllUser
from manageclient.models import MemberClient
from managejobs.models import Jobs


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
        new_job = Jobs(job_title='testjob',
                        job_number='1',
                        location='testlocation',
                        start_date='now',
                        end_date='tomorrow',
                        member=member,
                        client=client
                    )
        new_job.save()

        user_id = AllUser.objects.get(username='testadmin').pk
        job = Jobs.objects.get(member=member).pk
        print(job)
        new_form = CycleForm(member, {'cycle_title':'testjob',
                            'description':'testdescription',
                            'jobs': str(job)})

        self.assertTrue(new_form.is_valid())
        