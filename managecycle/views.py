from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import CycleForm#, EditCycleForm
from managejobs.view_func import get_all_jobs_for_user  
from .view_func import create_cycle, delete_all_files, clear_status
from .view_func import get_user_cycles, update_cycle
from accounts.models import AllUser
from managejobs.models import Jobs
from .models import Cycles  
from cyclestatus.models import CycleStatus

## Returns Manage Cycles Template with all User Cycles, ##
## and a form to create new user cycles ##
def manage_cycles(request, username):
    user = request.user
    cycle_form = CycleForm(user.pk)
    users_cycles = get_user_cycles(user)
    jobs = get_all_jobs_for_user(username, user.pk)
    if request.method == 'POST':
        create_cycle(user.pk, request.POST, user)
        if create_cycle:
            messages.success(request, 'A new cycle has been created',
                            extra_tags='manage_cycle')
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
    form = CycleForm(cycle.member.id, initial={'cycle_title': cycle.cycle_title,
                                        'description': cycle.description,
                                        'location': cycle.location,
                                        'start_date': cycle.start_date,
                                        'end_date': cycle.end_date,
                                        'jobs': cycle.job})
    if request.method == 'POST':
        form = CycleForm(cycle.member.id, request.POST)
        if form.is_valid():
            cycle_updated = update_cycle(cycle, form, request)
            if cycle_updated:
                messages.success(request, 
                                'You have updated cycle with Fileo ID: {0}'.format(cycle.id),
                                extra_tags='manage_cycle')
                return redirect(reverse('manage_cycles', kwargs={'username': username}))                                       

    return render(request, 'edit_cycle.html', {'username': username,
                                                'form': form })

## Delete Cycle View, redirects to Manage Cycles View ##
def delete_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    cycle.delete()
    messages.success(request, 'You have Deleted the Cycle with Fileo ID: {0}'.format(cycle_id),
                    extra_tags='manage_cycle')
    return redirect(reverse('manage_cycles', kwargs={'username':username}))

## Mark a Cycle as cancelled but don't delete ##
def cancel_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    status = get_object_or_404(CycleStatus, cycle=cycle)
    if request.POST['cancel'] == 'True':
        status.cancelled = True
        messages.success(request,   
                        'You have Cancelled the Cycle with the Fileo ID: {0}'.format(cycle.id),
                        extra_tags='manage_cycle')
    elif request.POST['cancel'] == 'False':
        messages.success(request,   
                        'You have Re-instated the Cycle with the Fileo ID: {0}'.format(cycle.id),
                        extra_tags='manage_cycle')
        status.cancelled = False

    status.save(update_fields=['cancelled'])
    return redirect(reverse('manage_cycles', kwargs={'username':username}))

## Reset Cycle Statuses and Delete Associated Files with that Cycle ##

def reset_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    clear_status(cycle)
    delete_all_files(request, cycle_id)
    messages.success(request,   
                    'You have Reset the Cycle with the Fileo ID: {0}'.format(cycle.id),
                    extra_tags='manage_cycle')
    return redirect(reverse('manage_cycles', kwargs={'username':username}))