from django.db import models
from django.contrib.auth.models import AbstractUser

### AUTHENTICATION MODEL FOR CLIENTS AND MEMBERS ###
class AllUser(AbstractUser):
    is_member = models.BooleanField(default=False)
    is_client = models.BooleanField(default=False)
    company = models.CharField(max_length=50, blank=True)
    phone = models.CharField(max_length=50, blank=True)
    position = models.CharField(max_length=50, blank=True)

    

### MODEL HOLDING MEMBER TO CLIENT RELATIONSHIPS ###

class MemberClient(models.Model):
    client = models.ForeignKey(AllUser, related_name='client', default=None, on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser, related_name='member', default=None, on_delete=models.CASCADE)
