from django.test import TestCase
from fileo.test_models import CreateTestModels

class TestCycleStatusModels(TestCase):

    def setUp(self):

        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()
        self.new_models.create_cycle_status()

    def test_get_cycle_status(self):

        cycle_status = self.new_models.get_cycle_status()
        
        self.assertTrue(cycle_status)
       