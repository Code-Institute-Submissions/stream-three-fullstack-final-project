import os
import shutil
from django.db import models
from django.http import Http404
from django.dispatch import receiver
from .models import Quotes, PurchaseOrder, Invoices

## Delete File From System on Deleting DB entry ##

@receiver(models.signals.post_delete, sender=Quotes)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """Delete File From System on Deleting DB entry"""

    client_path='media/quote/{0}/{1}/{2}'.format(instance.member,
                                        instance.client,
                                        instance.cycle.id)
    
    if instance.file:
        if os.path.isfile(instance.file.path):
            try:
                os.remove(instance.file.path)
            except OSError as e:
                print(e + 'error with auto delete signal')
                raise Http404
                
            try:
                shutil.rmtree(client_path)
                #print(client_path)
            except OSError as e:
                print(e)
                raise Http404