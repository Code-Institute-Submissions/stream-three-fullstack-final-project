from django.test import TestCase
from fileo.testing_models import CreateTestModels
from .view_func import get_all_clients_of_user

## TEST GET ALL CLIENTS BELONGING TO A MEMBER ##
class TestManageClientViewFunctionHelper(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
    
    def test_get_all_clients_of_user(self):
        self.models.create_profile()
        self.models.create_member_client()
        
        user_id = self.models.get_member().id
        clients = get_all_clients_of_user(user_id)

        self.assertTrue(clients)
        self.assertEqual(len(clients), 1)
        self.assertEqual(clients[0].client.username, 'testclient')
