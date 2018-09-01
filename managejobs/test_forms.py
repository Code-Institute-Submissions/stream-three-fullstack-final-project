from django.test import TestCase
from django.forms.models import model_to_dict
from .forms import JobsForm, EditJobsForm
from fileo.test_models import CreateTestModels

class TestJobsForms(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_job()
        self.models.create_cycle()
        self.models.create_profile()
        self.models.create_member_client()
        self.job = self.models.get_job()
        self.data = {'job_title':'test_job',
                    'client': self.models.get_client(),
                    'job_number':'123'} 


    def test_jobs_form(self):
        form = JobsForm(self.member.pk, self.data)
        self.assertTrue(form.is_valid())

    def test_edit_job(self):
        form = EditJobsForm(self.member.pk, self.data)
        self.assertTrue(form.is_valid())