from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import CycleForm, EditCycleForm
from .models import Cycles      
from .view_func import create_cycle
from .view_func import get_user_cycles, update_cycle
from accounts.models import AllUser
from managejobs.view_func import get_all_jobs_for_user
from managejobs.models import Jobs

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
                            'cycles': users_cycles[0],
                            'cycles_count': users_cycles[1],
                            'jobs': jobs})

## Edit Cycle and Redirect to Manage Cycles ##
def edit_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    form = EditCycleForm(cycle.member.id, initial={'cycle_title': cycle.cycle_title,
                                        'description': cycle.description,
                                        'location': cycle.location,
                                        'start_date': cycle.start_date,
                                        'end_date': cycle.end_date,
                                        'jobs': cycle.job,
                                        'cancelled': cycle.cancelled})
    if request.method == 'POST':
        form = EditCycleForm(cycle.member.id, request.POST)
        if form.is_valid():
            cycle_updated = update_cycle(cycle, form)
            if cycle_updated:
                messages.success(request, 
                                'You have updated cycle with Fileo ID: {0}'.format(cycle.id))
                return redirect(reverse('manage_cycles', kwargs={'username': username}))                                       

    return render(request, 'edit_cycle.html', {'username': username,
                                                'form': form })

## Delete Cycle View, redirects to Manage Cycles View ##
def delete_cycle(request, username, cycle_id):
    if request.method == 'POST':
        cycle = get_object_or_404(Cycles, pk=cycle_id)
        cycle.delete()
    return redirect(reverse('manage_cycles', kwargs={'username':username}))