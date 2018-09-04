from django.test import TestCase, RequestFactory
from fileo.testing_models import CreateTestModels
from django.contrib.sessions.middleware import SessionMiddleware
from .views import manage_jobs, delete_job

## TEST MANAGE JOB APP VIEWS ##
class TestManageJobsViews(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_job()

    def test_manage_jobs_view(self):
        url = 'profile/manage_jobs/{0}'.format(self.member.username)
        request = RequestFactory().get(url)
        request.user = self.member
        SessionMiddleware().process_request(request)
        request.session.save()

        response = manage_jobs(request, self.member.username)  

        self.assertEqual(response.status_code, 200)

    def test_delete_job(self):
        url = '/profile/manage_jobs/{0}/{1}/delete'.format(self.member.username,
                                                           self.models.get_job().pk)
        response = self.client.post(url)

        self.assertEqual(response.status_code, 302)