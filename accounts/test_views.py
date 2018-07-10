from django.test import TestCase
from django.shortcuts import get_object_or_404
from .models import AllUser

class TestAccountsViews(TestCase):
    def test_get_landing_page(self):
        page = self.client.get('/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'index.html')


    def test_get_registration(self):
        page = self.client.get('/accounts/register')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'register.html')