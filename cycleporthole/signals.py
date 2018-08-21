import os
import boto3
import botocore
import shutil
from fileo.settings import MEDIA_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME
from django.db import models
from django.http import Http404
from django.dispatch import receiver
from .models import Quotes, PurchaseOrder, Invoices

## Receiver Helper Function ##
def remove_file_from_aws(instance):    
    s3 = boto3.resource('s3')
    try:
        obj = s3.Object('fileo', 'media/{0}'.format(str(instance.file)))
        obj.delete()
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == '404':
            print('Error deleting file: {0}'.format(e))
            raise Http404


## RECEIVERS ##
## Delete Cycle Quotes File on Deleting DB field ## 
@receiver(models.signals.post_delete, sender=Quotes)
def auto_delete_quote_file(sender, instance, **kwargs):
    remove_file_from_aws(instance)
    
## Delete Cycle PO file on Deleting DB field ## 
@receiver(models.signals.post_delete, sender=PurchaseOrder)
def auto_delete_po_file(sender, instance, **kwargs):
    remove_file_from_aws(instance)

## Delete Cycle Invoice File on Deleting DB field ##
@receiver(models.signals.post_delete, sender=Invoices)
def auto_delete_invoice_file(sender, instance, **kwargs):
    remove_file_from_aws(instance)

