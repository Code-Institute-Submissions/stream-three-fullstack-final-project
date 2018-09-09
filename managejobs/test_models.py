from django.test import TestCase
from fileo.testing_models import CreateTestModels


class TestJobsModel(TestCase): 

    def setUp(self):
        self.models = CreateTestModels()
        self.models.create_job()

    def test_jobs_model(self):
        job = self.models.get_job()

        self.assertTrue(job)