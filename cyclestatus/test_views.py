from django.test import TestCase, RequestFactory
from fileo.testing_models import CreateTestModels
from django.contrib.sessions.middleware import SessionMiddleware
from .views import set_quote_status, set_invoice_status, set_po_status

## TEST CYCLE STATUS VIEWS REDIRECT ##
class TestCycleStatusViews(TestCase):

    def setUp(self):
        self.new_models = CreateTestModels()
        self.job = self.new_models.create_job()
        self.cycle = self.new_models.create_cycle()
        self.status = self.new_models.create_cycle_status()

    def test_set_quote_status(self):
        request = RequestFactory().get('porthole/quote/{0}/{1}'.format( 
                                            self.new_models.get_member().username,
                                            self.new_models.get_cycle().id))
        request.user = self.new_models.get_member()
        SessionMiddleware().process_request(request)
        request.session.save()

        response = set_quote_status(request, self.new_models.get_member().username, 
                                             self.new_models.get_cycle().id)

        self.assertEqual(response.status_code, 302)

    def test_set_invoice_status(self):
        request = RequestFactory().get('porthole/invoice/{0}/{1}'.format( 
                                            self.new_models.get_member().username,
                                            self.new_models.get_cycle().id))
        request.user = self.new_models.get_member()
        SessionMiddleware().process_request(request)
        request.session.save()

        response = set_invoice_status(request, self.new_models.get_member().username, 
                                             self.new_models.get_cycle().id)

        self.assertEqual(response.status_code, 302)

    def test_set_po_status(self):
        request = RequestFactory().get('porthole/po/{0}/{1}'.format( 
                                            self.new_models.get_member().username,
                                            self.new_models.get_cycle().id))
        request.user = self.new_models.get_member()
        SessionMiddleware().process_request(request)
        request.session.save()

        response = set_po_status(request, self.new_models.get_member().username, 
                                             self.new_models.get_cycle().id)

        self.assertEqual(response.status_code, 302)
