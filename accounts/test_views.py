from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import AllUser

class TestAccountsViews(TestCase):
    def test_get_landing_page(self):
        page = self.client.get('/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')

    def test_get_member_cycles(self):
        page =  self.client.get('/accounts/member/admin/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'member_cycles.html')

    def test_get_client_cycles(self):
        page = self.client.get('/accounts/client/client/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'client_cycles.html')