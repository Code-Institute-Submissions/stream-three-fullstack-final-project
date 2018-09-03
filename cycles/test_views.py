from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from django.shortcuts import get_object_or_404
from accounts.models import AllUser
from fileo.testing_models import CreateTestModels
from cycles.views import member_cycles, client_cycles, reset_search


class TestAccountsViews(TestCase):
    
    def setUp(self):
        self.new_models = CreateTestModels()
        self.factory = RequestFactory()
        self.middleware = SessionMiddleware()


    def test_get_member_cycles(self):
        request =  self.factory.get('/cycles/member/testadmin/')
        request.user = self.new_models.member
       
        self.middleware.process_request(request)
        request.session.save()
        response = member_cycles(request, 'testadmin')
    
        self.assertEqual(response.status_code, 200)

    def test_get_client_cycles(self):
        request = self.factory.get('/cycles/client/client/')
        request.user = self.new_models.client
        self.middleware.process_request(request)
        request.session.save()
        response = client_cycles(request, 'testclient')

        self.assertEqual(response.status_code, 200)
     
    def test_reset_search_for_member(self):
        request = self.factory.get('/cycles/testadmin/reset-search')
        request.user = self.new_models.client
        self.middleware.process_request(request)
        request.session.save()
        response = reset_search(request, 'testadmin')   

        self.assertEqual(response.status_code, 302)

    def test_reset_search_for_client(self):
        request = self.factory.get('/cycles/testclient/reset-search')
        request.user = self.new_models.client
        self.middleware.process_request(request)
        request.session.save()
        response = reset_search(request, 'testclient')   

        self.assertEqual(response.status_code, 302)