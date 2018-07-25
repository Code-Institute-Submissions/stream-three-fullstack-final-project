from django.shortcuts import get_object_or_404
from managecycle.models import Cycles
from accounts.models import AllUser
from .models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import QuoteStatus, POStatus, InvoicesStatus


## View helper functions/classes ##

## Class retrieving File Objects based on Cycle ID ##
## For use in Template to establish if a file has already ##
## been uploaded for each step ##

## Retrieve File from File Models for Download/Viewing ##
class GetFile:
    
    def __init__(self, cycle):
        self.cycle = cycle

    def get_quote(self):
        try:
            quote = Quotes.objects.get(cycle=self.cycle)
        except Quotes.DoesNotExist:
            quote = None
        return quote

    def get_po(self):
        try:
            po = PurchaseOrder.objects.get(cycle=self.cycle)
        except PurchaseOrder.DoesNotExist:
            po = None
        return po

    def get_invoice(self):
        try:
            invoice = Invoices.objects.get(cycle=self.cycle)
        except Invoices.DoesNotExist:
            invoice = None
        return invoice

### Get the Approval Status of Each Cycle Step ###
class GetStepStatus:
    
    def __init__(self, cycle):
        self.cycle = cycle
        self.quote = GetFile(self.cycle.id).get_quote()
        self.po = GetFile(self.cycle.id).get_po()
        self.invoice = GetFile(self.cycle.id).get_invoice()
        
        
    def get_quote_status(self):
        try:
            status = QuoteStatus.objects.get(quote=self.quote)
        except QuoteStatus.DoesNotExist:
            status = None
        #print(status.approve)
        return status

    def get_po_status(self):
        try:
            status = POStatus.objects.get(po=self.po)
        except POStatus.DoesNotExist:
            status = None

        return status

    def get_invoice_status(self):
        try:
            status = InvoicesStatus.objects.get(invoice=self.invoice)
        except InvoicesStatus.DoesNotExist:
            status = None

        return status

