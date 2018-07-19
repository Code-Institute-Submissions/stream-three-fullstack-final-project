from django.db import models
from accounts.models import AllUser
from jobs.models import Jobs

class Cycles(models.Model):
    cycle_title = models.CharField(max_length=50, blank=False)
    description = models.CharField(max_length=150, blank=False)
    member = models.ForeignKey(AllUser, 
                                related_name='member_cycle', 
                                on_delete=models.CASCADE)
    client = models.ForeignKey(AllUser, 
                                related_name='member_client',
                                on_delete=models.CASCADE,
                                null=True)
    job = models.ForeignKey(Jobs, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return '{0}-{1}'.format(self.cycle_title, self.description)

