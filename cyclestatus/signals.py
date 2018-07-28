from django.dispatch import receiver
from django.db import models
from managecycle.models import Cycles
from cyclestatus.models import CycleStatus

## Receiver writes entry into Status Model's when a new cycle is ##
## created.This means a reverse query on Cycles for each user can be ##
## done in the Cycles View App ##
@receiver(models.signals.post_save, sender=Cycles)
def set_default_quote_status(sender, instance, **kwargs):
    CycleStatus(cycle=instance).save()
    return True
    

