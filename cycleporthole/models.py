import os
from django.db import models
from django.core.validators import FileExtensionValidator
from djmoney.models.fields import MoneyField
from djmoney.money import Money
from djmoney.models.validators import MaxMoneyValidator, MinValueValidator
from accounts.models import AllUser
from managecycle.models import Cycles

## Determine upload path depending on whether instance is ##
## a quote, po or invoice ## 
def get_upload_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    
    try:
        if instance.is_quote:
            file_type = 'quote'
    except AttributeError as e:
        print('File is not a Quote: Error: {0}'.format(e))
    
    try:
        if instance.is_po:
            file_type = 'po'
    except AttributeError as e:
        print('File is not a PO: Error: {0}'.format(e))

    try:
        if instance.is_invoice:
            file_type = 'invoice'
    except AttributeError as e:
        print('File is not an Invoice: Error: {0}'.format(e))
    
    path ='{0}/{1}/{2}/{4}/{0}_{1}_{2}_{3}_{4}{5}'.format(file_type,
                                                instance.member,
                                                instance.client,
                                                instance.cycle.job.job_title,
                                                instance.cycle.id,
                                                ext) 
    return path

### BASE MODEL FOR QUOTE, PO, AND INVOICES ###
class UploadModel(models.Model):

    file = models.FileField(upload_to=get_upload_path, blank=False,
            validators=[FileExtensionValidator(allowed_extensions=['pdf'])])
    uploaded_at = models.DateTimeField()
    
    class Meta:
        abstract = True

                                            
class Quotes(UploadModel):                            
    client = models.ForeignKey(AllUser,related_name='QuotesUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='QuotesMemberFK', on_delete=models.CASCADE)
    cycle = models.OneToOneField(Cycles, related_name='QuotesCycleFK', 
                                on_delete=models.CASCADE, primary_key=True)
    is_quote = models.BooleanField(default=True)


    def __str__(self):
        return "{0} {1} {2} {3}".format(self.uploaded_at,
                                            self.client, self.member, 
                                            self.cycle)

class PurchaseOrder(UploadModel):
    client = models.ForeignKey(AllUser,related_name='POUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='POMemberFK', on_delete=models.CASCADE)
    cycle = models.OneToOneField(Cycles, related_name='POCycleFK', 
                                    on_delete=models.CASCADE, primary_key=True)
    is_po = models.BooleanField(default=True)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.uploaded_at,
                                        self.client, self.member, 
                                        self.cycle)

class Invoices(UploadModel):
    client = models.ForeignKey(AllUser,related_name='InvoiceUserFK', on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='InvoiceMemberFK', on_delete=models.CASCADE)
    cycle = models.OneToOneField(Cycles, related_name='InvoiceCycleFK', 
                                on_delete=models.CASCADE, primary_key=True)
    is_invoice = models.BooleanField(default=True)

    def __str__(self):
        return "{0} {1} {2} {3}".format(self.uploaded_at,
                                            self.client, self.member, 
                                            self.cycle)


