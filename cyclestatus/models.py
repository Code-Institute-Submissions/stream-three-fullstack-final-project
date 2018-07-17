from django.db import models

# Create your models here.

class CycleStatus(models.Model):
    approve = models.BooleanField(default=False, blank=False)
    contest = models.BooleanField(default=False, blank=False)
    urgent = models.BooleanField(default=False, blank=False)
    comment = models.BooleanField(default=False, blank=False)

    class Meta:
        abstract = True
        
    def __string__(self):
        return "{0}-{1}-{2}-{3}".format(self.approve, self.contest,
                                        self.urgent, self.comment)

#class QuoteStatus(CycleStatus):
