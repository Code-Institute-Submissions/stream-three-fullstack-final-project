from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import CycleForm
from .models import Cycles      
from .view_func import create_cycle
from .view_func import get_user_cycles
from accounts.models import AllUser
from managejobs.view_func import get_all_jobs_for_user

##  Returns Manage Cycles Template with all User Cycles, ##
## and a form to create new user cycles ##

def manage_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    cycle_form = CycleForm(user.pk)
    users_cycles = get_user_cycles(user)
    jobs = get_all_jobs_for_user(username, user.pk)
    if request.method == 'POST':
        create_cycle(user.pk, request.POST, user)
        if create_cycle:
            messages.success(request, "A new cycle has been created")
            return redirect(reverse('manage_cycles', kwargs={'username':user.username}))
    return render(request, 'manage_cycles.html', 
                            {'username':username,
                            'cycle_form':cycle_form,
                            'cycles': users_cycles,
                            'jobs': jobs})

## Delete Cycle View, redirects to Manage Cycles View ##
def delete_cycle(request, username, cycle_id):
    if request.method == 'POST':
        cycle = get_object_or_404(Cycles, pk=cycle_id)
        print(cycle)
        cycle.delete()
    return redirect(reverse('manage_cycles', kwargs={'username':username}))