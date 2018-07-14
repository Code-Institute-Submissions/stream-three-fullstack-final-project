from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CycleForm
from .models import Cycles      
from .view_func import create_cycle
from accounts.models import AllUser
from manageclient.models import MemberClient 

## Returns Member Cycles Template ##
def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    user_id = user.pk
    cycle_form = CycleForm(user_id)
    """ If post Create New Cycle """
    if request.method == 'POST':
        create_cycle(user_id, request.POST, user)
        if create_cycle:
            messages.success(request, "A new cycle has been created")
    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycle_form':cycle_form})

def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
