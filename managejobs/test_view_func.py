from django.test import TestCase
from managejobs import view_func
from fileo.test_models import CreateTestModels
from managejobs import view_func

## TEST MANAGE JOBS APP VIEW HELPERS ##
class TestManageJobsViewHelpers(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_job()
        self.models.create_profile()
        

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
        
