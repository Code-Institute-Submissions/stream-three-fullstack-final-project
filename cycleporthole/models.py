import os
import shutil
from django.http import Http404
from django.dispatch import receiver
from django.db import models
from django.core.validators import FileExtensionValidator
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinValueValidator
from accounts.models import AllUser
from cycles.models import Cycles

def get_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    print(ext)
    path='quotes/{0}/{1}/{3}/{0}_{1}_{2}_{3}{4}'.format(instance.member,
                                    instance.client,
                                    instance.cycle.job_title,
                                    instance.cycle.id,
                                    ext)
    return path

### BASE MODEL FOR QUOTE, PO, AND INVOICES ###
class UploadModel(models.Model):

    file = models.FileField(upload_to=get_upload_path, blank=False,
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self):
        return "{0} {1}".format(self.file, self.uploaded_at)
                                            
class Quotes(UploadModel):
    cycle_value = MoneyField(
                            max_digits=11,
                            default=0, 
                            decimal_places=1, 
                            default_currency='GBP'
                            )
                            
    client = models.ForeignKey(AllUser,related_name='QuotesUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='QuotesMemberFK', on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, related_name='QuotesCycleFK', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1} {2} {3} {4} {5}".format(self.file, self.uploaded_at,
                                            self.client, self.member, 
                                            self.cycle, self.cycle_value)

class PurchaseOrder(UploadModel):
    client = models.ForeignKey(AllUser,related_name='POUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='POMemberFK', on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, related_name='POCycleFK', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.file, self.uploaded_at,
                                            self.client, self.member, 
                                            self.cycle)

class Invoices(UploadModel):
    client = models.ForeignKey(AllUser,related_name='InvoiceUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='InvoiceMemberFK', on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles, related_name='InvoiceCycleFK', on_delete=models.CASCADE)

    def __str__(self):
        return "{0} {1} {2} {3} {4}".format(self.file, self.uploaded_at,
                                            self.client, self.member, 
                                            self.cycle)


