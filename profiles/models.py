from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from accounts.models import AllUser

# Create your models here.
class Profile(models.Model):

    company = models.CharField(max_length=50)
    address1 = models.CharField(max_length=50, blank=True)
    address2 = models.CharField(max_length=50, blank=True)
    city = models.CharField(max_length=50, blank=True)
    region = models.CharField(max_length=50, blank=True)
    post_code = models.CharField(max_length=10, blank=True)
    phone = PhoneNumberField(blank=True)
    position = models.CharField(max_length=50)
    user = models.ForeignKey(AllUser,on_delete=models.CASCADE)

    def __str__(self):
        return '{0}-{1}'.format(self.company, self.user)