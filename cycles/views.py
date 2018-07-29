from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.db.models import Q
from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from cyclestatus.models import CycleStatus#3, InvoicesStatus, POStatus
from managecycle.view_func import get_user_cycles
from accounts.models import AllUser
from manageclient.models import MemberClient 
from profiles.models import Profile
from profiles.view_func import profile_exists

## Helper Functions/Classes ##

## Search by Job Title, Cycle Title or Client ##
#(Q(cycle__job__job_title__contains=query)| Q(cycle__cycle_title__contains=query) | Q(cycle__client__first_name__contains=query | Q(cycle__client__firstname__contains=query)))
def search_member_cycles(request, username, query):
    cycles = CycleStatus.objects.filter(cycle__member__username=username).filter(
                                        Q(cycle__job__job_title__contains=query) | 
                                        Q(cycle__client__first_name__contains=query) | 
                                        Q(cycle__client__last_name__contains=query) | 
                                        Q(cycle__cycle_title__contains=query) | 
                                        Q(cycle__client__username__contains=query) |
                                        Q(cycle__id__contains=query)
                                        #Q(cycle__job__job_number__contains=query)
                                        )
    return cycles
    
## Returns Member Cycles Template with all User Cycles ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    is_existing = profile_exists(user.pk)
    if 'search' in request.GET:
        if request.GET['search']:
            q = request.GET['search']
            users_cycles = search_member_cycles(request, username, q)       
    else:
        users_cycles = CycleStatus.objects.filter(cycle__member=user)

    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycles': users_cycles,
                        'profile':is_existing})


## Returns Client Cycles Template with all Client Cycles ##
def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
