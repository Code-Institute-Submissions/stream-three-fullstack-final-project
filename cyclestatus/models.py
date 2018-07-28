from django.db import models
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles

## Models to store Boolean Fields about Approval Statuses of each Cycle Step ##
class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    #cancelled = models.BooleanField(default=False)
    #comment = models.TextField(max_length=150, blank=True)
    
    class Meta:
        abstract = True
       
class QuoteStatus(CycleStatus):
    quote = models.OneToOneField(Quotes, 
                                on_delete=models.CASCADE, 
                                primary_key=True)
    def __str__(self):
        return "{0}".format(self.quote)

class POStatus(CycleStatus):
    po = models.OneToOneField(PurchaseOrder,
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return "{0}".format(self.po)

class InvoicesStatus(CycleStatus):
    invoice = models.OneToOneField(Invoices,
                                    on_delete=models.CASCADE,
                                    primary_key=True)

    def __str__(self):
        return "{0}".format(self.invoice)

###############################################################
