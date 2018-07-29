from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
import datetime
from django.contrib import messages

## Class containing methods to push files to Relevant Model ##
## If the file model already contains an entry, it is deleted ##
## before writing the new entry. A signal is used to delete the actual PDF 
## to ensure only one file exists for each step in a cycle. ##

class UploadFile:
    
    def __init__(self, client, member, cycle):
        self.client = client
        self.member = member
        self.cycle = cycle
    
    def upload_quote(self, quote_form):
        new_quote = Quotes(file=quote_form.cleaned_data['file'],
                            uploaded_at=datetime.datetime.now(),
                            client=self.client,
                            member=self.member,
                            cycle=self.cycle)
                            #cycle_value=quote_form.cleaned_data['cycle_value'])
        try:
            old_quote = Quotes.objects.get(cycle=self.cycle)
        except Quotes.DoesNotExist:
            old_quote = None
        if old_quote:
            old_quote.delete()
            new_quote.save()
            print('Old Quote Deleted, New Saved')
        elif not old_quote:
            new_quote.save()
            print('Quote Saved')
            
    def upload_po(self, po_form):
        new_po = PurchaseOrder(file=po_form.cleaned_data['file'],
                                uploaded_at=datetime.datetime.now(),
                                client=self.client,
                                member=self.member,
                                cycle=self.cycle)
        try:
            old_po = PurchaseOrder.objects.get(cycle=self.cycle)
        except PurchaseOrder.DoesNotExist:
            old_po = None
        if old_po:
            old_po.delete()
            new_po.save()
            print('Old po Deleted, New Saved')
        elif not old_po:
            new_po.save()
            print('PO Saved')

        return True

    def upload_invoice(self, invoice_form):
        new_invoice = Invoices(file=invoice_form.cleaned_data['file'],
                                uploaded_at=datetime.datetime.now(),
                                client=self.client,
                                member=self.member,
                                cycle=self.cycle)
        try:
            old_invoice = Invoices.objects.get(cycle=self.cycle)
        except Invoices.DoesNotExist:
            old_invoice = None
        if old_invoice:
            old_invoice.delete()
            new_invoice.save()
            print('Old Invoice Deleted, New Saved')
        elif not old_invoice:
            new_invoice.save()
            print('Invoice Saved')
            
        return True
