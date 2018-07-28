from django.shortcuts import get_object_or_404
from managecycle.models import Cycles
from django.contrib import messages
from accounts.models import AllUser
from .models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import QuoteStatus, POStatus, InvoicesStatus
from cyclestatus.forms import StatusForm
from manageclient.models import MemberClient


## View helper functions/classes ##

## Get Context for Porthole View ##
def get_porthole_context(cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    profile = get_object_or_404(MemberClient, client=cycle.client.id)
    context = {'member': cycle.member,
                'client': cycle.client,
                'client_profile': profile,
                'status_form':StatusForm(),
                'cycle': cycle,
                'quote': GetFile(cycle).get_quote(),
                'po': GetFile(cycle).get_po(),
                'invoice': GetFile(cycle).get_invoice(),
                'quote_status': GetStepStatus(cycle).get_quote_status(),
                'po_status': GetStepStatus(cycle).get_po_status(),
                'invoice_status': GetStepStatus(cycle).get_invoice_status()
                 }
    return context


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

class DeleteFile:
    def __init__(self, request, cycle_id):
        self.request = request
        self.cycle_id = cycle_id

    def delete_quote(self):
        quote = GetFile(self.cycle_id).get_quote()
        if quote:
            quote.delete()
            messages.success(self.request, 
                            'You successfully deleted your Quote.',
                                extra_tags='quote_delete')
        else:
            messages.error(self.request, 
                            "You haven't uploaded a file yet. There is nothing to delete.",
                            extra_tags='quote_delete')
        return True

    def delete_po(self):
        po = GetFile(self.cycle_id).get_po()
        if po:
            po.delete()
            messages.success(self.request, 
                            'You successfully deleted your Purchase Order.',
                            extra_tags='po_delete')
        else:
            messages.error(self.request, 
                            "You haven't uploaded a file yet. There is nothing to delete.",
                            extra_tags='po_delete')
        return True
        

    def delete_invoice(self):
        invoice = GetFile(self.cycle_id).get_invoice()
        if invoice:
            invoice.delete()
            messages.success(self.request, 
                            'You successfully deleted your Invoice.',
                        extra_tags='invoice_delete')
        else:
            messages.error(self.request, 
                            "You haven't uploaded a file yet. There is nothing to delete.",
                            extra_tags='invoice_delete')
        return True