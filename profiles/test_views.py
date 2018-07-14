from django.test import TestCase
from accounts.models import AllUser

class TestProfilesViews(TestCase):
  
    def test_get_member_profile_view(self):
        AllUser.objects.create_user(first_name='testadmin',
                                    last_name='test',
                                    username='testadmin',
                                    email='testadmin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )
        page =  self.client.get('/profile/edit/testadmin/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'member_profile.html')