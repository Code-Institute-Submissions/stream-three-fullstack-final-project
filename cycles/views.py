from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect, reverse
from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from cyclestatus.models import CycleStatus
from accounts.models import AllUser
from manageclient.models import MemberClient 
from profiles.models import Profile
from managecycle.view_func import get_user_cycles
from .view_func import get_searched_cycles, SetSessionValues
from profiles.view_func import profile_exists
from search.search import SearchCycles

## Returns Member Cycles Template with All Cycles or Searched User Cycles ##
## for the user as a Member ##
def member_cycles(request, username):
    SetSessionValues(request).set_values()
    is_existing = profile_exists(request.user.pk)
    users_cycles = CycleStatus.objects.filter(
                                            cycle__member=request.user
                                           ).order_by('-cycle__created')
    if 'search' in request.GET:
        users_cycles = get_searched_cycles(request)                   
        return render(request,
                        'cycles.html', 
                        {'user':request.user,
                        'cycles': users_cycles,
                        'profile':is_existing,
                        'search': request.GET }) 
    return render(request,
                    'cycles.html', 
                    {'user':request.user,
                    'cycles': users_cycles,
                    'profile':is_existing,
                    'search': None })

## Returns Member Cycles Template with All Cycles or Searched User Cycles ##
## for the user as a Client. ##
def client_cycles(request, username):
    SetSessionValues(request).set_values()
    users_cycles = CycleStatus.objects.filter(
                                            cycle__client=request.user
                                           ).order_by('-cycle__created')
    print(users_cycles)
    if 'search' in request.GET:
        users_cycles = get_searched_cycles(request)
        return render(request,
                        'cycles.html', 
                        {'user':request.user,
                        'cycles': users_cycles,
                        'search': request.GET })

    
    return render(request,
                'cycles.html', 
                {'user':request.user,
                'cycles': users_cycles,
                'search': None })



## Redirects Back to Member Cycles to Clear Search ##
def reset_search(request, username):
    if request.user.is_member:
        return redirect(reverse('member_cycles',kwargs={'username':username}))
    if request.user.is_client:
        return redirect(reverse('client_cycles', kwargs={'username':username}))