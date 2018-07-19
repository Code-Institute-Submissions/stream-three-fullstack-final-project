from django.db import models
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from cycles.models import Cycles

# Create your models here.

## Models to store Boolean Fields about Approval Statuses of each Cycle Step ##
class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    comment = models.TextField(max_length=150, blank=True)
    action = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = True
       
class QuoteStatus(CycleStatus):
    quote = models.OneToOneField(Quotes, 
                                on_delete=models.CASCADE, 
                                primary_key=True)
    def __str__(self):
        return "{0}".format(self.quote)

class POStatus(CycleStatus):
    po = models.OneToOneField(PurchaseOrder)

    def __str__(self):
        return "{0}".format(self.po)

class InvoicesStatus(CycleStatus):
    invoice = models.OneToOneField(Invoices)

    def __str__(self):
        return "{0}".format(self.invoice)

###############################################################

## Models to store file submission Urgency Statuses for Each Cycle Step ##
class Urgency(models.Model):
    urgent = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = True

class QuoteUrgency(Urgency):
    cycle = models.OneToOneField(Cycles, 
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return "{0}".format(self.cycle)    


class POUrgency(Urgency):
    cycle = models.OneToOneField(Cycles, 
                                on_delete=models.CASCADE,
                                primary_key=True)
    def __str__(self):
        return "{0}".format(self.cycle)    

class InvoiceUrgency(Urgency):
    cycle = models.OneToOneField(Cycles, 
                                on_delete=models.CASCADE,
                                primary_key=True)

    def __str__(self):
        return "{0}".format(self.cycle)    
