from django.test import TestCase
from .view_func import set_status, email_status
from .forms import StatusForm
from fileo.testing_models import CreateTestModels

## TEST CYCLE STATUS VIEW HELPER FUNCTIONS/CLASSES ##
class TestCycleStatusViewHelpers(TestCase):

    def setUp(self):
        self.approve_form = StatusForm({'status' : 'approve'})
        self.contest_form = StatusForm({'status' : 'contest'})
        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()  
        self.new_models.create_profile()

    def test_set_approve_status_to_true(self):
        status = set_status(self.approve_form)

        self.assertEqual(status[0], True)
        self.assertEqual(status[1], False)

    def test_set_contest_status_to_true(self):
        status = set_status(self.contest_form)

        self.assertEqual(status[0], False)
        self.assertEqual(status[1], True)

    def test_email_status_is_sent(self):
        email = email_status(self.new_models.get_member().username,
                            self.new_models.get_client().username,
                            self.new_models.get_cycle().id,
                            self.approve_form,
                            'quote')

        self.assertTrue(email)