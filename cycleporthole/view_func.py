from django.shortcuts import get_object_or_404
from managecycle.models import Cycles
from accounts.models import AllUser
from .models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import QuoteStatus, POStatus, InvoicesStatus


## View helper functions/classes ##

## Class retrieving File Objects based on Cycle ID ##
## For use in Template to establish if a file has already ##
## been uploaded for each step ##

## Get Cycle Info for Porthole View #
def get_porthole_info(username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    porthole_info = {'cycle': cycle,
                    'member': cycle.member, 
                    'client': cycle.client, 
                    'quote': GetFile(cycle).get_quote(),
                    'po': GetFile(cycle).get_po(),
                    'invoice': GetFile(cycle).get_invoice()}
    return porthole_info

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
    
    def __init__(self, cycle_id):
        self.cycle_id = cycle_id
        self.cycle = get_object_or_404(Cycles, pk=self.cycle_id)
        self.quote = GetFile(self.cycle_id).get_quote()
        self.po = GetFile(self.cycle_id).get_quote()
        self.invoice = GetFile(self.cycle_id).get_quote()
        
        
    def get_status_of_quote(self):
        try:
            status = QuoteStatus.objects.get(quote=self.quote)
        except QuoteStatus.DoesNotExist:
            status = None

        return status

    def get_status_of_po(self):
        try:
            status = POStatus.objects.get(po=self.po)
        except POStatus.DoesNotExist:
            status = None

        return status

    def get_status_of_invoice(self):
        try:
            status = InvoicesStatus.objects.get(invoice=self.invoice)
        except POStatus.DoesNotExist:
            status = None

        return status