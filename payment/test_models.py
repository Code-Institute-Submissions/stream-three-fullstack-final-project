from django.test import TestCase
from fileo.testing_models import CreateTestModels

class TestPaymentModels(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.models.create_job()
        self.models.create_cycle()
        self.models.create_payment()

    def test_order_model(self):
        order = self.models.get_payment()

        self.assertTrue(order)