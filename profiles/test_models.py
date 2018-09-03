from django.test import TestCase
from accounts.models import AllUser
from .models import Profile
from fileo.testing_models import CreateTestModels

class TestProfileModel(TestCase):

    def setUp(self):
        new_models = CreateTestModels()
        new_models.create_profile()
        self.profile = new_models.get_profile()
        
    def test_create_profile(self):
        profile = self.profile

        self.assertEqual(profile.company, 'Test Company')
        self.assertEqual(profile.phone, '+441784938491')
        self.assertEqual(profile.position, 'Boss')
       