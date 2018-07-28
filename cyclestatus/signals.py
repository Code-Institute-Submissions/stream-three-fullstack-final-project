from django.dispatch import receiver
from django.db import models
from managecycle.models import Cycles
from cyclestatus.models import CycleStatus

## Receiver writes entry into Status Model's when a new cycle is ##
## created.This means a reverse query on Cycles for each user can be ##
## done on the status
@receiver(models.signals.post_save, sender=Cycles)
def set_default_quote_status(sender, instance, **kwargs):
    quote_status = QuoteStatus(cycle=instance)
    quote_status.save()
    return True
    
@receiver(models.signals.post_save, sender=Cycles)
def set_default_po_status(sender, instance, **kwargs):
    po_status = POStatus(cycle=instance)
    po_status.save()
    return True

@receiver(models.signals.post_save, sender=Cycles)
def set_default_invoice_status(sender, instance, **kwargs):
    invoice_status = InvoicesStatus(cycle=instance)
    invoice_status.save()
    return True

