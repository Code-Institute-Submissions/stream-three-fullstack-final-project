from django.test import TestCase
from accounts.models import AllUser
from .models import Profile

class TestProfileModel(TestCase):

    def test_create_profile(self):
        AllUser.objects.create_user(first_name='testadmin',
                                    last_name='test',
                                    username='testadmin',
                                    email='testadmin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )

        user = AllUser.objects.get(username='testadmin')
        new_profile = Profile(company='Test Company',
                                phone='+441784938491',
                                position='Boss',
                                user=user)

        new_profile.save()
        get_profile = Profile.objects.get(user=user.pk)

        self.assertEqual(get_profile.company, 'Test Company')
        self.assertEqual(get_profile.phone, '+441784938491')
        self.assertEqual(get_profile.position, 'Boss')
       