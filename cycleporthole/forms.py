import PyPDF2
from django.template.defaultfilters import filesizeformat
from django.conf import settings
from django import forms
from django.forms import ModelForm
from djmoney.forms import MoneyField
from PyPDF2.utils import PdfReadError
from .models import Quotes, PurchaseOrder, Invoices

## UPLOAD FORM BASE CLASS ##
class UploadForm(ModelForm):
    file = forms.FileField(label='')
    
    def clean_file(self):
        pdf_file = self.cleaned_data['file']
        try:
            PyPDF2.PdfFileReader(pdf_file)
        except PdfReadError:
            raise forms.ValidationError('Please make sure your file is a PDF.')
        
        if pdf_file.size > settings.MAX_UPLOAD_SIZE:
            size = filesizeformat(settings.MAX_UPLOAD_SIZE)
            raise forms.ValidationError('Please keep filesize under {0}.'.format(size))
            
        return pdf_file 

## QUOTE FORM INHERITS BASE, BUT ADDS A CYCLE VALUE INPUT FIELD ##
class QuotesForm(UploadForm):
    cycle_value = MoneyField(min_value=0,
                            max_value = 999999,
                            currency_choices=[('GBP','Pound Sterling')],
                            label='',
                            required=True)
    step_type = forms.CharField(widget=forms.HiddenInput(attrs={'value':'quote'}))

    class Meta:
        model = Quotes
        fields = ['file']

## PO FORM INHERITS FROM BASE WITH NO CYCLE VALUE INPUT FIELD ##
class PurchaseOrderForm(UploadForm):
    step_type = forms.CharField(widget=forms.HiddenInput(attrs={'value':'po'}))
                                   
    class Meta:
        model = PurchaseOrder
        fields = ['file']

## INVOICE FORM INHERITS FROM BASE WITH NO CYCLE VALUE INPUT FIELD ##
class InvoiceForm(UploadForm):
    step_type = forms.CharField(widget=forms.HiddenInput(attrs={'value':'invoice'}))
                                                            
    class Meta:
        model = Invoices
        fields = ['file']