import PyPDF2
from django import forms
from django.forms import ModelForm
from PyPDF2.utils import PdfReadError
from .models import Quotes, PurchaseOrder, Invoices

## Upload Form Base Class ##
class UploadForm(ModelForm):
    file = forms.FileField()

    def clean_pdf(self):
        pdf_file = self.cleaned_data['file']
        try:
            PyPDF2.PdfFileReader(pdf_file)
        except PdfReadError:
            raise forms.ValidationError('This is not a PDF file.')
        return pdf_file

class QuotesForm(UploadForm):
    cycle_value = forms.CharField()
    class Meta:
        model = Quotes
        fields = ['file', 'cycle_value']

class PurchaseOrderForm(UploadForm):
    class Meta:
        model = PurchaseOrder
        fields = ['file']

class InvoiceForm(UploadForm):
    class Meta:
        model = Invoices
        fields = ['file']