from django.test import TestCase
from fileo.test_models import CreateTestModels

class TestMemberClient(TestCase):
    
    def setUp(self):
        new_models =CreateTestModels()
        new_models.create_profile()
        new_models.create_member_client()
        self.member = new_models.get_member()
        self.client = new_models.get_client()
        self.member_client = new_models.get_member_client()
        

    def test_member_client_model(self):
        self.assertEqual(self.member_client.member, self.member)
        self.assertEqual(self.member_client.client, self.client)