from django.test import TestCase, RequestFactory
from django.contrib.sessions.middleware import SessionMiddleware
from fileo.test_models import CreateTestModels
from .views import porthole, step_notify, delete_file


## TEST PORTHOLE VIEWS ##
class TestCyclePortholeViews(TestCase):
    ## Build Model Objects ##
    def setUp(self):
        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()
        self.new_models.create_profile()
        self.new_models.create_member_client()
        self.factory = RequestFactory()
        self.middleware = SessionMiddleware()
        self.member = self.new_models.get_member()
        self.clients = self.new_models.get_client()
        self.cycle = self.new_models.get_cycle()
 
    def test_porthole_view(self):
        url = '/porthole/member/{0}/{1}/{2}/'.format(self.member.username,
                                                    self.clients.username,
                                                    self.cycle.id)
        request = self.factory.get(url)
        request.user = self.member
        self.middleware.process_request(request)
        request.session.save()
        response = porthole(request, self.member.username, self.cycle.id)
        
        self.assertEqual(response.status_code, 200)
  
    def test_step_notify_view(self):
        url = '/porthole/member/{0}/{1}/{2}/notify'.format(self.member.username,
                                                self.clients.username,
                                                self.cycle.id)
        step = 'quote'
        request = self.factory.get(url)
        request.user = (self.member)
        self.middleware.process_request(request)
        request.session.save()
        response = step_notify(request, self.member.username, self.cycle.id, step)

       
        self.assertEqual(response.status_code, 302)
  
    def test_delete_file(self):
        url = '/porthole/member/{0}/{1}/{2}/delete'.format(self.member.username,
                                                self.clients.username,
                                                self.cycle.id)
        step = 'quote'
        request = self.factory.get(url)
        request.user = (self.member)
        self.middleware.process_request(request)
        request.session.save()
        response = delete_file(request, self.member.username, self.cycle.id, step)

        self.assertEqual(response.status_code, 302)

