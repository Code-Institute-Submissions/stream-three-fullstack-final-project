from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from managecycle.view_func import get_user_cycles
from accounts.models import AllUser
from manageclient.models import MemberClient 
from profiles.models import Profile
from profiles.view_func import profile_exists

## Returns Member Cycles Template with all User Cycles ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    users_cycles = get_user_cycles(user)
    is_existing = profile_exists(user.pk)

    all_info = Cycles.objects.select_related('QuotesCycleFK').filter(member=user)
    #print(all_info)
    #print(all_info.cycle_value)
   

    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycles': users_cycles[0],
                            'profile':is_existing})





def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
