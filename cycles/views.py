from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from managecycle.view_func import get_user_cycles
from accounts.models import AllUser
from manageclient.models import MemberClient 


def member_cycles(request, username):
    """ Returns Member Cycles Template with all User Cycles """
    user = get_object_or_404(AllUser, username=username)
    users_cycles = get_user_cycles(user)
    
    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycles': users_cycles})





def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
