from django.test import TestCase
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from djmoney.money import Money
from django.core.files.uploadedfile import SimpleUploadedFile

## TEST PORTHOLE UPLOAD FORMS ##
class TestCyclePortholeForms(TestCase):

## TEST FORMS WON'T BE VALID DUE TO INVALID PDF ##

    def test_quotes_form_not_valid(self):
        file = SimpleUploadedFile('file.pdf', b'file_content')
        form = QuotesForm({'cycle_value': Money(1, 'GBP')},
                            {'file': file})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['file'], 
                        [u'Please make sure your file is a PDF.'])
    
    def test_po_form_not_valid(self):
        file = SimpleUploadedFile('file.pdf', b'file_content')
        form = PurchaseOrderForm({'cycle_value': Money(1, 'GBP')},
                            {'file': file})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['file'], 
                        [u'Please make sure your file is a PDF.'])
    def test_invoices_form_not_valid(self):
        file = SimpleUploadedFile('file.pdf', b'file_content')
        form = InvoiceForm({'cycle_value': Money(1, 'GBP')},
                            {'file': file})

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['file'], 
                        [u'Please make sure your file is a PDF.'])