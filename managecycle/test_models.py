from django.test import TestCase
from fileo.test_models import CreateTestModels


## TEST MANAGE CYCLE MODEL ##
class TestCyclesModel(TestCase):
    
    def setUp(self):
        new_models = CreateTestModels()
        new_models.create_job()
        new_models.create_cycle()
        self.cycle = new_models.get_cycle()
        self.member = new_models.get_member()
        self.client = new_models.get_client()

        
    def test_create_a_cycle(self):
        cycle = self.cycle

        self.assertEqual(cycle.member, self.member)
        self.assertEqual(cycle.client, self.client)