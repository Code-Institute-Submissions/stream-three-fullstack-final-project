from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from cyclestatus.models import CycleStatus#3, InvoicesStatus, POStatus
from managecycle.view_func import get_user_cycles
from accounts.models import AllUser
from manageclient.models import MemberClient 
from profiles.models import Profile
from profiles.view_func import profile_exists


## Returns Member Cycles Template with all User Cycles ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    is_existing = profile_exists(user.pk)
    users_cycles = CycleStatus.objects.filter(cycle__member=user)
   
    ## Write Sort Queries for Cycles, Retrieve Statuses ##

    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycles': users_cycles,
                            'profile':is_existing})





def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
