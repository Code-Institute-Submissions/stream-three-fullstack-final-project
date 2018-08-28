from datetime import datetime
from django.shortcuts import get_object_or_404
from managecycle.models import Cycles
from django.contrib import messages
from accounts.models import AllUser
from .models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import CycleStatus
from cyclestatus.forms import StatusForm
from manageclient.models import MemberClient

## View helper functions/classes ##

## CONVERT DATES TO MORE READABLE STRING ##
def convert_dates(date):
    date = datetime.strptime(date, '%Y-%m-%d')
    date = '{0}.{1}.{2}'.format(date.day, date.month, date.year)
    return date

## Get Context for Porthole View ##
def get_porthole_context(cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    #profile = get_object_or_404(MemberClient, client=cycle.client.id)
    context = {'member': cycle.member,
                'client': cycle.client,
                #'client_profile': profile,
                'status_form': StatusForm(),
                'cycle': cycle,
                'cycle_start': convert_dates(cycle.start_date),
                'cycle_end': convert_dates(cycle.end_date),
                'quote': GetFile(cycle).get_quote(),
                'po': GetFile(cycle).get_po(),
                'invoice': GetFile(cycle).get_invoice(),
                'cycle_status': CycleStatuses(cycle).get_cycle_status()
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
class CycleStatuses:
    
    def __init__(self, cycle):
        self.cycle= cycle
        try:
            self.cycle_status = CycleStatus.objects.get(cycle=self.cycle)
        except CycleStatus.DoesNotExist:
            self.cycle_status = None
        
    def get_cycle_status(self):
        return self.cycle_status

    ## Set Pending Payment Status based on Step Approval Statuses ##
    def set_pending(self):
        if (self.cycle_status.approve_quote and 
            self.cycle_status.approve_po and 
            self.cycle_status.approve_invoice and not
            self.cycle_status.complete):
            
            self.cycle_status.pending = True
            self.cycle_status.save(update_fields=['pending'])
        else:
            self.cycle_status.pending = False
            self.cycle_status.save(update_fields=['pending'])


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
                                extra_tags='quote', fail_silently=True)
        return True

    def delete_po(self):
        po = GetFile(self.cycle_id).get_po()
        if po:
            po.delete()
            messages.success(self.request, 
                            'You successfully deleted your Purchase Order.',
                            extra_tags='po', fail_silently=True)
        return True
        

    def delete_invoice(self):
        invoice = GetFile(self.cycle_id).get_invoice()
        if invoice:
            invoice.delete()
            messages.success(self.request, 
                            'You successfully deleted your Invoice.',
                        extra_tags='invoice', fail_silently=True)
        return True