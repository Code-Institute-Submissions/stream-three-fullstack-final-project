from django.db import models
from managecycle.models import Cycles

## Models to store Boolean Fields about Approval Statuses of each Cycle Step ##

class CycleStatus(models.Model):
    approve_quote = models.BooleanField(default=False, blank=True)
    contest_quote = models.BooleanField(default=False, blank=True)
    approve_po = models.BooleanField(default=False, blank=True)
    contest_po = models.BooleanField(default=False, blank=True)
    approve_invoice = models.BooleanField(default=False, blank=True)
    contest_invoice = models.BooleanField(default=False, blank=True)
    complete = models.BooleanField(default=False, blank=True)
    pending = models.BooleanField(default=False, blank=True)
    cancelled = models.BooleanField(default=False, blank=True)
    cycle = models.OneToOneField(Cycles,
                                related_name='quote_status',
                                on_delete=models.CASCADE, 
                                primary_key=True)
    def __str__(self):
        return "{0}".format(self.cycle)
