from django.test import TestCase
from django.forms.models import model_to_dict
from django.shortcuts import get_object_or_404
from .forms import CycleForm
from accounts.models import AllUser
from manageclient.models import MemberClient
from managejobs.models import Jobs
from fileo.test_models import CreateTestModels
from .models import Cycles

class TestCycleForm(TestCase):
    
    def setUp(self):
        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()
    
    def test_cycle_form_is_not_valid(self):
        user_id = AllUser.objects.get(username=self.new_models.member).pk
        new_form = CycleForm(user_id)

        self.assertFalse(new_form.is_valid())
           
    def test_cycle_form_is_valid(self):
        member = self.new_models.get_member()
        cycle = Cycles.objects.get(member=member)
        new_form = CycleForm(member, {'cycle_title': cycle.cycle_title,
                                        'description': cycle.description,
                                        'location': cycle.location,
                                        'start_date': cycle.start_date,
                                        'end_date': cycle.end_date,
                                        'jobs': cycle.job.pk})

        self.assertTrue(new_form.is_valid())
        