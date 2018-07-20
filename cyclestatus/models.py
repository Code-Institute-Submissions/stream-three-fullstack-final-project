from django.db import models
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles

## Models to store Boolean Fields about Approval Statuses of each Cycle Step ##
class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    comment = models.TextField(max_length=150, blank=True)
    
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
"""
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

####################################################################

## Models to store whether Action is Needed for a Cycle Step ##
class Action(models.Model):
    action = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = True

class QuoteAction(Action):
    quote = models.OneToOneField(Quotes,
                                on_delete=models.CASCADE,
                                primary_key=True)
    
    def __str__(self):
        return "{0}".format(self.quote)

class POAction(Action):
    po = models.OneToOneField(PurchaseOrder,
                                on_delete=models.CASCADE,
                                primary_key=True)
    
    def __str__(self):
        return "{0}".format(self.po)

class InvoiceAction(Action):
    invoice = models.OneToOneField(Invoices,
                            on_delete=models.CASCADE,
                            primary_key=True)
    
    def __str__(self):
        return "{0}".format(self.invoice)
"""