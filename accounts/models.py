from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser

### AUTHENTICATION MODEL FOR CLIENTS AND MEMBERS. ###
### ADDED IS_MEMBER AND IS_CLIENT TO BASE USER MODEL. ###
### BOOLEAN USED DETERMINE THE TYPE OF USER IN ###
### EACH TEMPLATE, USE TEMPLATE LOGIC TO SHOW ###
### TAILORED TEMPLATES FOR EACH USER TYPE. ###

class AllUser(AbstractUser):
    is_member = models.BooleanField(default=True)
    is_client = models.BooleanField(default=False)
  
    

