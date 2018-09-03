from django.test import TestCase
from django.forms.models import model_to_dict
from .forms import ProfileForm
from .models import Profile
from accounts.models import AllUser
from fileo.testing_models import CreateTestModels

class TestProfileForm(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()

    def test_create_new_profile_form(self):
        user = self.models.get_member()
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
        profile = self.models.get_profile()
        new_form = ProfileForm(model_to_dict(profile))

        self.assertTrue(new_form.is_valid())
