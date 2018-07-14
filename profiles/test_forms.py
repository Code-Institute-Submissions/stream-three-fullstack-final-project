from django.test import TestCase
from .forms import ProfileForm

class TestProfileForm(TestCase):

    def test_create_new_profile_form(self):
        new_form = ProfileForm({'company':'Test Company',
                    'phone': '+441784938491',
                    'position': 'Boss'})

        self.assertTrue(new_form.is_valid())
