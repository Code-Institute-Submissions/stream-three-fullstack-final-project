from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import CycleStatus
from django.utils import timezone
from django.contrib import messages
from .view_func import GetFile  

## Class containing methods to push files to Relevant Model ##
## If the file model already contains an entry, it is deleted ##
## before writing the new entry. A signal is used to delete the actual PDF 
## to ensure only one file exists for each step in a cycle. ##

## HELPER FUNCTIONS ##

def get_cycle_status(cycle):
    try:
        status = CycleStatus.objects.get(cycle=cycle)
    except CycleStatus.DoesNotExist:
        status = None
    return status
    
## CHECK IF QUOTE IS APPROVED ##
def is_quote_approved(cycle):
    quote_approved = get_cycle_status(cycle)
    if quote_approved:
        return quote_approved.approve_quote
    else:
        return None
    
## CHECK IF PO IS APPROVED ##
def is_po_approved(cycle):
    po_approved = get_cycle_status(cycle)
    if po_approved:
        return po_approved.approve_po
    else:
        return None
    

class UploadFile:
    
    def __init__(self, client, member, cycle):
        self.client = client
        self.member = member
        self.cycle = cycle

    def upload_quote(self, quote_form):
        new_quote = Quotes(file=quote_form.cleaned_data['file'],
                            uploaded_at=timezone.now(),
                            client=self.client,
                            member=self.member,
                            cycle=self.cycle)
                        
       
        old_quote = GetFile(self.cycle).get_quote()
       
        if old_quote:
            old_quote.delete()
            new_quote.save()
        elif not old_quote:
            new_quote.save()

        return True
            
    ## CHECK FIRST IF A QUOTE IS EXISTING ##
    ## USE BOOLEAN IN VIEW TO RAISE ERROR IF NOT EXISTING ##
    ## DOESN'T MAKE SENSE TO BE ABLE TO UPLOAD A PO WITHOUT ##
    ## A QUOTE ##
    def upload_po(self, po_form):
        new_po = PurchaseOrder(file=po_form.cleaned_data['file'],
                                uploaded_at=timezone.now(),
                                client=self.client,
                                member=self.member,
                                cycle=self.cycle)
        get_file = GetFile(self.cycle)
        old_po = get_file.get_po()

        approved_quote = is_quote_approved(self.cycle)

        if approved_quote:
            if old_po:
                old_po.delete()
                new_po.save() 
            elif not old_po:
                new_po.save()
            return True
        else:
            return False

    ## CHECK FIRST IF A PO IS EXISTING ##
    ## USE BOOLEAN IN VIEW TO RAISE ERROR IF NOT EXISTING ##
    ## DOESN'T MAKE SENSE TO BE ABLE TO UPLOAD A PO WITHOUT ##
    ## A PO ##
    def upload_invoice(self, invoice_form):
        new_invoice = Invoices(file=invoice_form.cleaned_data['file'],
                                uploaded_at=timezone.now(),
                                client=self.client,
                                member=self.member,
                                cycle=self.cycle)
        
        get_file = GetFile(self.cycle)
        old_invoice = get_file.get_invoice()

        approved_po = is_po_approved(self.cycle)
        
        if approved_po:
            if old_invoice:
                old_invoice.delete()
                new_invoice.save()
            elif not old_invoice:
                new_invoice.save()
            return True
        else:
            return False  
            
