from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

### AUTHENTICATION MODEL FOR CLIENTS AND MEMBERS ###
class AllUser(AbstractUser):
    is_member = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
    #company = models.CharField(max_length=50, blank=True)
    #phone = models.CharField(max_length=20, null=True, blank=True)
    #position = models.CharField(max_length=50, blank=True)
    #is_member = models.NullBooleanField()
    #is_client = models.NullBooleanField()
    

