from django.db import models
# Create your models here.
from accounts.models import AllUser
### MODEL HOLDING MEMBER TO CLIENT RELATIONSHIPS ###

class MemberClient(models.Model):
    client = models.ForeignKey(AllUser, related_name='client', default=None, on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='member', default=None, on_delete=models.CASCADE)