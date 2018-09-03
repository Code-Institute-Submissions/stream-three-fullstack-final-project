from django.test import TestCase, RequestFactory
from fileo.testing_models import CreateTestModels
from django.contrib.sessions.middleware import SessionMiddleware
from .views import payment


## TEST PAYMENT APP VIEWS ##
class TestPaymentViews(TestCase):

    def setUp(self):
        self.models = CreateTestModels()
        self.member = self.models.get_member()
        self.models.create_cycle()
        self.cycle = self.models.get_cycle()

    def test_payment_view(self):
        url = ('payment/{0}/{1}'.format(self.member.username, self.cycle.pk))

        request = RequestFactory.get(url)
        request.user = self.member
        SessionMiddleware.process_request(url)
        request.session.save()

        response = payment(request, self.member.username, self.cycle.pk)

        self.assertEqual(response.status, 200)