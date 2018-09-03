from django.test import TestCase
from managejobs import view_func
from fileo.test_models import CreateTestModels
from managejobs import view_func
from .forms import JobsForm, EditJobsForm
from .models import Jobs

## TEST MANAGE JOBS APP VIEW HELPERS ##
class TestManageJobsViewHelpers(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_job()
        self.models.create_profile()
        self.data = {'job_title':'new job',
                    'client': self.models.get_client(),
                    'job_number':'123'} 

    def test_get_all_jobs_for_user(self):
        jobs = view_func.get_all_jobs_for_user(self.member.id)

        self.assertTrue(jobs)
        self.assertEqual('test job', jobs[0].job_title)
        self.assertEqual(len(jobs), 1)

    def test_the_user_has_clients(self):
        self.models.create_member_client()
        clients = view_func.does_the_user_have_clients(self.member.username,
                                                        self.member.pk)
        self.assertTrue(clients)

    def test_the_user_doesnt_have_clients(self):
        clients = view_func.does_the_user_have_clients(self.member.username,
                                                        self.member.pk)
        self.assertFalse(clients)

    def test_create_job(self):
        self.models.create_member_client()
        form = JobsForm(self.member.pk, self.data)
        if form.is_valid():
            view_func.create_job(form, self.member)
        job = Jobs.objects.get(job_title='new job')

        self.assertTrue(job)
        self.assertEqual(job.job_title, self.data['job_title'])
        self.assertEqual(job.job_number, self.data['job_number'])
        self.assertEqual(job.member, self.member)
        self.assertEqual(job.client, self.models.get_client())

    def test_update_job(self):
        self.models.create_member_client()
        form = JobsForm(self.member.pk, self.data)
        if form.is_valid():
            view_func.create_job(form, self.member)
        job = Jobs.objects.get(job_title='new job')
        update_form = EditJobsForm(self.member.pk, {'job_title':'update job',
                                                    'job_number': '123',
                                                    'client':self.models.get_client()})
        if update_form.is_valid():
            view_func.update_job(job, update_form)

        updated_job = Jobs.objects.get(job_title='update job')

        self.assertEqual(updated_job.job_title, 'updated job')