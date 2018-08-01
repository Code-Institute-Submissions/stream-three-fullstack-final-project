from django.test import TestCase
from .forms import ProfileForm
from .models import Profile
from django.forms.models import model_to_dict
from accounts.models import AllUser

class TestProfileForm(TestCase):
    def setUp(self):
        AllUser.objects.create_user(first_name='testadmin',
                                    last_name='test',
                                    username='testadmin',
                                    email='testadmin@email.com',
                                    password='password',
                                    is_member=True,
                                    is_client=False
                                    )

    def test_create_new_profile_form(self):
        user = AllUser.objects.get(username='testadmin')
        new_profile = Profile(company='Test Company',
                                phone='+441784938491',
                                position='Boss',
                                address1='address1',
                                address2='address2',
                                city='city',
                                region='region',
                                post_code='post_code',
                                country='GB',
                                user=user)

        new_profile.save()
        profile = Profile.objects.get(user=user)
        new_form = ProfileForm(model_to_dict(profile))

        self.assertTrue(new_form.is_valid())
