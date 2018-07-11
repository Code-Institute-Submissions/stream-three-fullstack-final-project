from django.db import models
from accounts.models import AllUser

class Cycles(models.Model):

    #company = models.CharField(max_length=50, blank=True)
    job_title = models.CharField(max_length=50, blank=False)
    location = models.CharField(max_length=50, blank=True)
    description = models.CharField(max_length=50, blank=False)
    member = models.ForeignKey(AllUser, related_name='member_cycle', on_delete=models.CASCADE)
    client = models.ForeignKey(AllUser, related_name='client_cycle', on_delete=models.CASCADE)

    def __str__(self):
        return '{0}-{1}'.format(self.job_title, self.location)

