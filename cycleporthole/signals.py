import os
import shutil
from django.db import models
from django.http import Http404
from django.dispatch import receiver
from .models import Quotes, PurchaseOrder, Invoices

## Delete Cycle File From Model on Deleting DB entry ##

## Receiver Helper Function ##
def remove_file_on_delete_helper(instance, client_path):
    if instance.file:
        if os.path.isfile(instance.file.path):
            try:
                os.remove(instance.file.path)
            except OSError as e:
                print(e + 'error with auto delete signal')
                raise Http404
                
            try:
                shutil.rmtree(client_path)
            except OSError as e:
                print(e)
                raise Http404

## RECEIVERS ##

## Delete Cycle Quotes File on Deleting DB entry ## 
@receiver(models.signals.post_delete, sender=Quotes)
def auto_delete_quote_file(sender, instance, **kwargs):
    client_path='media/quote/{0}/{1}/{2}'.format(instance.member,
                                        instance.client,
                                        instance.cycle.id)
    remove_file_on_delete_helper(instance, client_path)
    

## Delete Cycle PO file on Deleting DB entry ## 
@receiver(models.signals.post_delete, sender=PurchaseOrder)
def auto_delete_po_file(sender, instance, **kwargs):
    client_path='media/po/{0}/{1}/{2}'.format(instance.member,
                                        instance.client,
                                        instance.cycle.id)
    remove_file_on_delete_helper(instance, client_path)

## Delete Cycle Invoice File on Deleting DB entry ##
@receiver(models.signals.post_delete, sender=Invoices)
def auto_delete_invoice_file(sender, instance, **kwargs):
    client_path='media/invoice/{0}/{1}/{2}'.format(instance.member,
                                        instance.client,
                                        instance.cycle.id)
    remove_file_on_delete_helper(instance, client_path)
    