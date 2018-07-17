from django.shortcuts import get_object_or_404
from cycles.models import Cycles
from accounts.models import AllUser
from .models import Quotes, PurchaseOrder, Invoices


## View helper functions ##

## Class retrieving File Objects based on Cycle ID ##
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


## Get Cycle Info for Porthole View #
    
def get_porthole_info(username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    member = get_object_or_404(AllUser, username=username)
    client = get_object_or_404(AllUser, username=client_username)
    porthole_info = {'cycle':cycle,
                    'member': member, 
                    'client':client, 
                    'quote': GetFile(cycle).get_quote(),
                    'po': GetFile(cycle).get_po(),
                    'invoice': GetFile(cycle).get_invoice()}
    return porthole_info