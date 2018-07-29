from django.shortcuts import render, get_object_or_404, redirect, reverse

from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from cyclestatus.models import CycleStatus
from managecycle.view_func import get_user_cycles
from accounts.models import AllUser
from manageclient.models import MemberClient 
from profiles.models import Profile
from profiles.view_func import profile_exists
from search.search import SearchCycles

## Helper Functions/Classes ##
    
## Returns Member Cycles Template with all User Cycles ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    is_existing = profile_exists(user.pk)
    if 'search' in request.GET:
        search = request.GET['search']
        kwargs = {'search': search}
        users_cycles = SearchCycles(request, username, **kwargs
                                    ).search_member_cycles() 
        return render(request,'member_cycles.html', 
                    {'username':username,
                    'cycles': users_cycles,
                    'profile':is_existing,
                    'search': search }) 
    else:
        users_cycles = CycleStatus.objects.filter(
                                            cycle__member=user
                                            ).order_by('-cycle__created')

    return render(request,'member_cycles.html', 
                        {'username':username,
                        'cycles': users_cycles,
                        'profile':is_existing,
                        'search': None })


## Returns Client Cycles Template with all Client Cycles ##
def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
