from django.test import TestCase
from .forms import StatusForm

## TEST CYCLE STATUS FORM ##
class TestStatusForm(TestCase):
    
    def test_status_form(self):
        form = StatusForm({'status': 'approve'})
        self.assertTrue(form.is_valid())
