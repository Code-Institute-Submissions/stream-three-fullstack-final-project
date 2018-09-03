from django.test import TestCase
from fileo.testing_models import CreateTestModels

class TestPaymentModels(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.models.create_job()
        self.models.create_cycle()