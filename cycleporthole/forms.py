import PyPDF2
from django import forms
from django.forms import ModelForm
from djmoney.forms import MoneyField
from PyPDF2.utils import PdfReadError
from .models import Quotes, PurchaseOrder, Invoices

## Upload Form Base Class ##
class UploadForm(ModelForm):
    file = forms.FileField(label='Upload PDF:')

    def clean_file(self):
        pdf_file = self.cleaned_data['file']
        print(pdf_file)
        try:
            PyPDF2.PdfFileReader(pdf_file)
        except PdfReadError:
            raise forms.ValidationError('This is not a PDF file.')
        return pdf_file

class QuotesForm(UploadForm):
    cycle_value = MoneyField(min_value=0,
                            currency_choices=[('GBP','Pound Sterling'),
                                                ('EUR','Euro')]
                            )

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