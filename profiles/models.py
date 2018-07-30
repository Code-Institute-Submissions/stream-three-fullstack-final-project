from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django_countries.fields import CountryField
from accounts.models import AllUser

## Profile Base Class inherited by Profile Model and Order Model ##
class ProfileBase(models.Model):
    address1 = models.CharField(max_length=50, blank=False)
    address2 = models.CharField(max_length=50, blank=False)
    city = models.CharField(max_length=50, blank=False)
    region = models.CharField(max_length=50, blank=False)
    post_code = models.CharField(max_length=10, blank=False)
    country = CountryField(default='United Kingdom',blank=False)
    phone = PhoneNumberField(blank=False)
    
    class Meta:
        abstract = True

class Profile(ProfileBase):
    company = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    user = models.ForeignKey(AllUser,on_delete=models.CASCADE)

    def __str__(self):
        return '{0}-{1}'.format(self.company, self.user)