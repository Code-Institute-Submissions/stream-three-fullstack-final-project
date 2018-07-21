from django.db import models
from accounts.models import AllUser
from profiles.models import Profile


### MODEL HOLDING MEMBER TO CLIENT AND PROFILE RELATIONSHIPS ###

class MemberClient(models.Model):
    client = models.ForeignKey(AllUser, 
                                related_name='client', 
                                default=None, 
                                on_delete=models.CASCADE)
    member = models.ForeignKey(AllUser,
                                related_name='member', 
                                default=None, 
                                on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,
                                related_name='profile', 
                                default=None, 
                                on_delete=models.CASCADE,
                                blank=True,
                                null=True)
                                
    def __str__(self):
        return "{0}".format(self.client)