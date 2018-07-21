from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import CycleForm
from .models import Cycles      
from .view_func import create_cycle
from cycles.view_func import get_user_cycles
from accounts.models import AllUser
#from manageclient.models import MemberClient 

def manage_cycles(request, username):
    """ Returns Manage Cycles Template with all User Cycles """
    user = get_object_or_404(AllUser, username=username)
    user_id = user.pk
    cycle_form = CycleForm(user_id)
    users_cycles = get_user_cycles(user)
    #print(users_cycles)
    """ If post Create New Cycle """
    if request.method == 'POST':
        create_cycle(user_id, request.POST, user)
        if create_cycle:
            messages.success(request, "A new cycle has been created")
            return redirect(reverse('member_cycles', kwargs={'username':user.username}))
    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycle_form':cycle_form,
                            'cycles': users_cycles})