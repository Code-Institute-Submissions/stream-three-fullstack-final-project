from django.test import TestCase, RequestFactory
from fileo.testing_models import CreateTestModels
from django.contrib.sessions.middleware import SessionMiddleware
from .views import manage_cycles, cancel_cycle, reset_cycle, delete_cycle

## TEST MANAGECYCLE APP VIEWS ##
class TestCyclesViews(TestCase):
    
    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_job()
        self.models.create_cycle()
        self.cycle = self.models.get_cycle()

    def test_manage_cycle(self):
        url = 'profile/manage_cycles/{0}'.format(self.member.username)

        request = RequestFactory().get(url)
        request.user = self.member
        SessionMiddleware().process_request(request)
        request.session.save()
        response = manage_cycles(request, self.member.username)

        self.assertEqual(response.status_code, 200)

    def test_delete_cycle(self):
        url = '/profile/manage_cycles/{0}/{1}/delete'.format(self.member.username,
                                                            self.cycle.pk)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)

    def test_cancel_cycle(self):
        url = '/profile/manage_cycles/{0}/{1}/cancel'.format(self.member.username,
                                                        self.cycle.pk)

        request = RequestFactory().post(url, {'cancel':'cancel'})

        request.user = self.member
        SessionMiddleware().process_request(request)
        request.session.save()
        response = cancel_cycle(request, self.member.username, self.cycle.pk)

        self.assertEqual(response.status_code, 302)

    def test_reset_cycle(self):
        url = '/profile/manage_cycles/{0}/{1}/reset'.format(self.member.username,
                                                        self.cycle.pk)

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)
