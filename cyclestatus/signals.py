from django.dispatch import receiver
from django.db import models
from managecycle.models import Cycles
from cyclestatus.models import CycleStatus
from cycleporthole.models import Quotes, PurchaseOrder, Invoices

## Receiver writes entry into Status Model's when a new cycle is ##
## created.This means a reverse query on Cycles for each user can be ##
## done in the Cycles View App ##
@receiver(models.signals.post_save, sender=Cycles)
def set_default_quote_status(sender, instance, **kwargs):
    CycleStatus(cycle=instance).save()
    return True
    
## Receiver to Reset the Approval status of a Quote ##
## should a new file be uploaded ##
@receiver(models.signals.post_save, sender=Quotes)
def reset_quote_status(sender, instance, **kwargs):
    try:
        quote_status = CycleStatus(cycle=instance.cycle)
    except CycleStatus.DoesNotExist:
        quote_status = None
    
    if quote_status:
        quote_status.approve_quote = False
        quote_status.contest_quote = False
        quote_status.save(update_fields=['approve_quote', 
                                        'contest_quote'])
    return True

## Receiver to Reset the Approval status of a PO ##
## should a new file be uploaded ##
@receiver(models.signals.post_save, sender=PurchaseOrder)
def reset_po_status(sender, instance, **kwargs):
    try:
        po_status = CycleStatus(cycle=instance.cycle)
    except CycleStatus.DoesNotExist:
        po_status = None
        
    if po_status:
        po_status.approve_po = False
        po_status.contest_po = False
        po_status.save(update_fields=['approve_po',
                                        'contest_po'])
    return True

## Receiver to Reset the Approval status of an Invoice ##
## should a new file be uploaded ##
@receiver(models.signals.post_save, sender=Invoices)
def reset_invoice_status(sender, instance, **kwargs):
    try:
        invoice_status = CycleStatus(cycle=instance.cycle)
    except CycleStatus.DoesNotExist:
        invoice_status = None
        
    if invoice_status:
        invoice_status.approve_invoice = False
        invoice_status.contest_invoice = False
        invoice_status.save(update_fields=['approve_invoice',
                                            'contest_invoice'])
    return True


#@receiver(models.signals.post_save, sender=CycleStatus)
#def set_payment_pending_if_invoice_approved(sender, instance, **kwargs):
    #quote_status = instance.approve_quote
    #po_status = instance.approve_po
    #invoice_status = instance.approve_invoice

    #if (quote_status and po_status and invoice_status):
     #   instance.pending = True
      #  instance.update(update_fields=['pending'])
    #else:
     #   instance.pending = False
      #  instance.update(update_fields=['pending'])




