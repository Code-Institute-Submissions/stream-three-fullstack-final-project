from django.test import TestCase
from django.shortcuts import get_object_or_404


class TestAccountsViews(TestCase):
    
    def test_get_manage_clients(self):
        page =  self.client.get('/profile/manage_clients/admin')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'manage_clients.html')

    