from django.contrib import messages
from managecycle.models import Cycles      

## Get all User Cycles ##
def get_user_cycles(user):
    try:
        users_cycles = Cycles.objects.filter(member=user)
    except Cycles.DoesNotExist:
        users_cycles = None
    return users_cycles