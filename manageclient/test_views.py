from django.test import TestCase
from django.shortcuts import get_object_or_404
from fileo.testing_models import CreateTestModels


class TestAccountsViews(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()
        
    def test_get_manage_clients(self):
        page =  self.client.get('/profile/manage_clients/admin')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'manage_clients.html')

    def test_delete_client(self):
        page =  self.client.get('/profile/manage_clients/admin/{0}'.format(
                                                            self.models.get_client().pk))
        self.assertEqual(page.status_code, 302)