from django.test import TestCase
from accounts.models import AllUser
from fileo.testing_models import CreateTestModels

## TEST PROFILE APP VIEWS ##
class TestProfilesViews(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()

    def test_get_member_profile_view(self):
        page =  self.client.get('/profile/edit/testadmin/')
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'member_profile.html')

    def test_get_client_profile_view(self):
        client_id = self.models.get_client().pk
        page =  self.client.get('/profile/edit/testclient/{0}'.format(client_id))
        
        self.assertEqual(page.status_code, 200)
        self.assertTemplateUsed(page, 'client_profile.html')