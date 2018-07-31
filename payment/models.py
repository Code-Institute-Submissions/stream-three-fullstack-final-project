from django.db import models
from profiles.models import ProfileBase
from managecycle.models import Cycles
from datetime import datetime

## Order model inherits from Profile Base Class ##
class Order(ProfileBase):
    name_on_card = models.CharField(max_length=50, blank=False)
    date = models.DateField(auto_now_add=datetime.now())

    def __str__(self):
        return '{0}-{1}'.format(self.name_on_card, self.date)
    
class OrderLineItem(models.Model):
    order = models.ForeignKey(Order, 
                                on_delete=models.CASCADE)
    cycle = models.ForeignKey(Cycles,
                                on_delete=models.CASCADE) 
    