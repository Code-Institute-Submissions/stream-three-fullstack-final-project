from django.db import models
from accounts.models import AllUser
from managejobs.models import Jobs
#from cyclestatus.models import QuotesStatus, POStatus, InvoicesStatus

## Model to store Cycle Info ##
class Cycles(models.Model):
    cycle_title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    start_date = models.CharField(max_length=50, blank=False)
    end_date = models.CharField(max_length=50, blank=False)
    member = models.ForeignKey(AllUser, 
                                related_name='member_cycle', 
                                on_delete=models.CASCADE,
                                )
    client = models.ForeignKey(AllUser, 
                                related_name='client_cycle',
                                on_delete=models.CASCADE,
                                )
    job = models.ForeignKey(Jobs, 
                            on_delete=models.CASCADE,
                            )
    #cancelled = models.BooleanField(default=False)
    #payment_pending = models.BooleanField(default=False)
    #completed = models.BooleanField(default=False)

    def __str__(self):
        return '{0}-{1}'.format(self.cycle_title, self.description)