from django.test import TestCase
from django.shortcuts import get_object_or_404
from accounts.models import AllUser


class TestAccountsViews(TestCase):
    
    def test_get_member_cycles(self):
        AllUser.objects.create_user(first_name='admin',
                                    last_name='test',
                                    username='admin',
                                    email='admin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )
        page =  self.client.get('/cycles/member/admin/')
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'member_cycles.html')

    def test_get_client_cycles(self):
        page = self.client.get('/cycles/client/client/')

        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'client_cycles.html')
