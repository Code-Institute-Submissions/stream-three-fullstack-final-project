from datetime import datetime
from django.db import models
from accounts.models import AllUser
from managejobs.models import Jobs
from djmoney.models.fields import MoneyField
from djmoney.money import Money

#from cyclestatus.models import QuotesStatus, POStatus, InvoicesStatus

## Model to store Cycle Info ##
class Cycles(models.Model):
    created = models.DateTimeField(auto_now_add=datetime.now())
    cycle_title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    start_date = models.CharField(max_length=50, blank=False)
    end_date = models.CharField(max_length=50, blank=False)
    cycle_value = MoneyField(
                        max_digits=11,
                        default=0, 
                        decimal_places=1, 
                        default_currency='GBP'
                        )
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

    def __str__(self):
        return '{0}-{1}'.format(self.cycle_title, self.description)