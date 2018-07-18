from django.db import models
from cycleporthole.models import Quotes, PurchaseOrder, Invoices

# Create your models here.

class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    urgent = models.BooleanField(default=False, blank=False)
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
