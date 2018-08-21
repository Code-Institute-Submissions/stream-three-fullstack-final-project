import os
import boto3
#from boto.s3.connection import S3Connection, Bucket, Key
import shutil
from fileo.settings import MEDIA_URL, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_REGION_NAME
from django.db import models
from django.http import Http404
from django.dispatch import receiver
from .models import Quotes, PurchaseOrder, Invoices


def remove_file_from_aws(instance):    
    s3 = boto3.resource('s3')
    obj = s3.Object('fileo', 'media/{0}'.format(str(instance.file)))
    obj.delete()
    
## Delete Cycle File From Model on Deleting DB entry ##
## Receiver Helper Function ##



## If file exists, delete it, then delete folder structure ##
def remove_file_on_delete_helper(instance, client_path):
    if instance.file:
        if os.path.isfile(instance.file.path):
            try:
                os.remove(instance.file.path)
            except OSError as e:
                print(e + 'error deleting file')
                raise Http404
                
            try:
                shutil.rmtree(client_path)
            except OSError as e:
                print(e + 'error deleting file directories')
                raise Http404

## RECEIVERS ##
## Delete Cycle Quotes File on Deleting DB field ## 
@receiver(models.signals.post_delete, sender=Quotes)
def auto_delete_quote_file(sender, instance, **kwargs):
    client_path='{0}/quote/{1}/{2}/{3}'.format(MEDIA_URL, 
                                                instance.member,
                                                instance.client,
                                                instance.cycle.id)

    
    remove_file_on_delete_helper(instance)
    #remove_file_from_aws(instance)
    

## Delete Cycle PO file on Deleting DB field ## 
@receiver(models.signals.post_delete, sender=PurchaseOrder)
def auto_delete_po_file(sender, instance, **kwargs):
    client_path='{0}/po/{1}/{2}/{3}'.format(MEDIA_URL, 
                                                instance.member,
                                                instance.client,
                                                instance.cycle.id)
    if os.path.exists('env.py'):
        remove_file_on_delete_helper(instance, client_path)

## Delete Cycle Invoice File on Deleting DB field ##
@receiver(models.signals.post_delete, sender=Invoices)
def auto_delete_invoice_file(sender, instance, **kwargs):
    client_path='{0}/invoice/{1}/{2}/{3}'.format(MEDIA_URL, 
                                                instance.member,
                                                instance.client,
                                                instance.cycle.id)
    if os.path.exists('env.py'):
        remove_file_on_delete_helper(instance, client_path)

