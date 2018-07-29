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
from .view_func import get_searched_cycles

## Helper Functions/Classes ##
    
## Returns Member Cycles Template with All Cycles or Searched User Cycles ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    is_existing = profile_exists(user.pk)
    users_cycles = CycleStatus.objects.filter(
                                            cycle__member=user
                                           ).order_by('-cycle__created')
    if 'search' in request.GET:
        users_cycles = get_searched_cycles(request, username)                   
        return render(request,
                        'member_cycles.html', 
                        {'username':username,
                        'cycles': users_cycles,
                        'profile':is_existing,
                        'search': request.GET }) 
    return render(request,
                    'member_cycles.html', 
                    {'username':username,
                    'cycles': users_cycles,
                    'profile':is_existing,
                    'search': None })

## Redirects Back to Member Cycles to Clear Search ##
def reset_search(request, username):
    
    return redirect(reverse('member_cycles'), username=username)

## Returns Client Cycles Template with all Client Cycles ##
def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
