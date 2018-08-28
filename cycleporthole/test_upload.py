from django.test import TestCase, RequestFactory
from cycleporthole import upload
from fileo.test_models import CreateTestModels

## TESTS FOR CYCLEPORTHOLE UPLOAD HELPER FUNCTIONS/CLASSES ##
class TestUploadHelpers(TestCase):

    def setUp(self):
        self.new_models = CreateTestModels()
        self.new_models.create_job()
        self.new_models.create_cycle()
        self.member = self.new_models.get_member()
        self.client = self.new_models.get_client()
        self.cycle = self.new_models.get_cycle()

    def test_step_isnt_approved(self):
        approved_quote = upload.is_quote_approved(self.cycle)
        approved_po = upload.is_po_approved(self.cycle)

        self.assertFalse(approved_quote)
        self.assertFalse(approved_po)

    def test_step_is_approved(self):
        status = self.new_models.get_cycle_status()
        status.approve_quote = True
        status.approve_po = True
        status.save(update_fields=['approve_quote',
                                    'approve_po'])
        
        approved_quote = upload.is_quote_approved(self.cycle)
        approved_po = upload.is_po_approved(self.cycle)
        
        self.assertTrue(approved_quote)
        self.assertTrue(approved_po)
    
    