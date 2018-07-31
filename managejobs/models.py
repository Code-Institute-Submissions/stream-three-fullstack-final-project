from django.utils import timezone
from django.db import models
from accounts.models import AllUser

## Function get Job last number for User and Increment by 1 ##

class Jobs(models.Model):
    created = models.DateTimeField(auto_now_add=timezone.now())
    job_title = models.CharField(max_length=50, blank=False)
    job_number = models.CharField(max_length=50, blank=False)
    member = models.ForeignKey(AllUser,
                                default=None,
                                related_name='jobs_member',
                                on_delete=models.CASCADE)
    client = models.ForeignKey(AllUser,
                                default=None,
                                related_name='jobs_client',
                                on_delete=models.CASCADE)

    def __str__(self):
        return "Job Title: {0}, Client: {1}".format(self.job_title, self.client)
