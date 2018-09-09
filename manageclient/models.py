from django.db import models
from django.utils import timezone
from accounts.models import AllUser
from profiles.models import Profile


### MODEL HOLDING MEMBER TO CLIENT RELATIONSHIPS. ###

class MemberClient(models.Model):
    created = models.DateTimeField(auto_now_add=timezone.now())
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