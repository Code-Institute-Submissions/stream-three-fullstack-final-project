import PyPDF2
from django.template.defaultfilters import filesizeformat
from django.conf import settings
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
        try:
            PyPDF2.PdfFileReader(pdf_file)
        except PdfReadError:
            raise forms.ValidationError('Please make sure your file is a PDF.')
        
        if pdf_file.size > settings.MAX_UPLOAD_SIZE:
            size = filesizeformat(settings.MAX_UPLOAD_SIZE)
            raise forms.ValidationError('Please keep filesize under {0}.'.format(size))
            
        return pdf_file

    #def clean_file(self):
      #  file = self.cleaned_data['file']
      #  print(file.size)
      #  if file.size > settings.MAX_UPLOAD_SIZE:
         #   print('fileisbigger')
          #  raise forms.ValidationError('Please keep filesize under {0}.'.format(filesizeformat(settings.MAX_UPLOAD_SIZE)))
        
       # return file


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