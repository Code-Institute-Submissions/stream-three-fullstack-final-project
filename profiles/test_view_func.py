from django.test import TestCase
from fileo.testing_models import CreateTestModels
from .forms import ProfileForm
from profiles import view_func 
from .models import Profile

## TEST PROFILE APP VIEW HELPER FUNCTIONS ##
class TestProfilesHelperFunctions(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.profile = self.models.create_profile()
        self.models.create_member_client()

    def test_profile_exists(self):
        profile = view_func.profile_exists(self.member.pk)
        self.assertTrue(profile)

    def test_edit_profile(self):
        edit_profile = ProfileForm({'company':'Edit Company',
                                   'position':'CEO',
                                    'phone':'+441234567890',
                                    'address1':'edit address1',
                                    'address2':'edit address2',
                                    'city':'edit city',
                                    'region':'edit region',
                                    'post_code':'edit post code',
                                    'country':'FR'})
        if edit_profile.is_valid():
            is_existing = view_func.profile_exists(self.member.pk)
            if is_existing:
                view_func.edit_profile(edit_profile, is_existing)
                edited_profile = self.models.get_profile()
        
        self.assertEqual(edited_profile.company, 'Edit Company')
        self.assertEqual(edited_profile.position, 'CEO')
        self.assertEqual(edited_profile.phone, '+441234567890')
        self.assertEqual(edited_profile.address1, 'edit address1')
        self.assertEqual(edited_profile.address2, 'edit address2')
        self.assertEqual(edited_profile.city, 'edit city')
        self.assertEqual(edited_profile.region, 'edit region')
        self.assertEqual(edited_profile.post_code, 'edit post code')
        self.assertEqual(edited_profile.country, 'FR')

    def test_new_profile(self):
        new_profile = ProfileForm({'company':'New Company',
                                   'position':' New CEO',
                                    'phone':'+441234567890',
                                    'address1':'New address1',
                                    'address2':'New address2',
                                    'city':'New city',
                                    'region':'New region',
                                    'post_code':'New post code',
                                    'country':'FR'})
        if new_profile.is_valid():
            view_func.new_profile(new_profile, self.member)
        profile = Profile.objects.get(company='New Company')
           
        self.assertEqual(profile.company, 'New Company')
        self.assertEqual(profile.position, 'New CEO')
        self.assertEqual(profile.phone, '+441234567890')
        self.assertEqual(profile.address1, 'New address1')
        self.assertEqual(profile.address2, 'New address2')
        self.assertEqual(profile.city, 'New city')
        self.assertEqual(profile.region, 'New region')
        self.assertEqual(profile.post_code, 'New post code')
        self.assertEqual(profile.country, 'FR')
        
    def test_add_client_profile_to_member_client(self):
        self.models.create_client_profile()
        profile = self.models.get_client_profile()
        client_id = self.models.get_client().pk
        added_profile = view_func.add_profile_in_member_client_model(client_id)
        member_client = self.models.get_member_client()

        self.assertTrue(added_profile)
        self.assertEqual(profile, member_client.profile)

        