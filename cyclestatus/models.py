from django.db import models
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles

## Models to store Boolean Fields about Approval Statuses of each Cycle Step ##
"""
class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = True
"""
       
class QuoteStatus():
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    cycle = models.OneToOneField(Cycles, 
                                on_delete=models.CASCADE, 
                                primary_key=True)
    def __str__(self):
        return "{0}".format(self.cycle)

class POStatus():
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    cycle = models.OneToOneField(Cycles,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return "{0}".format(self.cycle)

class InvoicesStatus():
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    cycle = models.OneToOneField(Cycles,
                                    on_delete=models.CASCADE,
                                    primary_key=True)

    def __str__(self):
        return "{0}".format(self.cycle)

###############################################################
