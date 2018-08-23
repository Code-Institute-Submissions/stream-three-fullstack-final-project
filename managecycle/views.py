from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from datetime import datetime
from .forms import CycleForm#, EditCycleForm
from managejobs.view_func import get_all_jobs_for_user  
from .view_func import create_cycle, delete_all_files, clear_status
from .view_func import get_user_cycles, update_cycle, clear_value
from cycleporthole.view_func import CycleStatuses
from accounts.models import AllUser
from managejobs.models import Jobs
from .models import Cycles  
from cyclestatus.models import CycleStatus
from cycles.view_func import SetSessionValues

## Return Manage Cycles Template ##
## User can see all Cyles and create new ones ##
## If Update Key in request.POST, render form with inital values ##
## If Updated in POST request run Update Helper instead of Create Helper ##
def manage_cycles(request, username):
    SetSessionValues(request).set_values()
    user = request.user
    cycle_form = CycleForm(user.pk)
    users_cycles = users_cycles = CycleStatus.objects.filter(
                                                cycle__member=user
                                                ).order_by('cycle__job__job_title')
   
    jobs = get_all_jobs_for_user(user.pk)
    if request.method == 'POST':
        if 'update' in request.POST.keys():
            cycle = get_object_or_404(Cycles, pk=(request.POST['cycle_id']))
            request.session['update_cycle_id'] = cycle.id
            start_date = datetime.strptime(cycle.start_date, '%Y-%m-%d')
            end_date = datetime.strptime(cycle.end_date, '%Y-%m-%d')
            cycle_form = CycleForm(cycle.member.id, 
                                    initial={'cycle_title': cycle.cycle_title,
                                    'description': cycle.description,
                                    'location': cycle.location,
                                    'start_date': start_date ,
                                    'end_date': end_date,
                                    'jobs': cycle.job})
        else:
            cycle_form = CycleForm(user.pk, request.POST)
            if cycle_form.is_valid():
                if 'updated' in request.POST.keys():
                    cycle = get_object_or_404(Cycles, pk=request.session['update_cycle_id'])
                    update_cycle(cycle, cycle_form)
                    messages.success(request, 'Cycle updated.', extra_tags='manage_cycle')
                    return redirect(reverse('manage_cycles', kwargs={'username':username}))
                else:
                    create_cycle(cycle_form, user)
                    messages.success(request, 'Cycle created.', extra_tags='manage_cycle')
            
                    return redirect(reverse('manage_cycles', kwargs={'username':username}))
    print(users_cycles.count())
    return render(request, 'manage_cycles.html', 
                            {'username': username,
                            'cycle_form':cycle_form,
                            'cycles': users_cycles,
                            #'cycles_count': users_cycles.count(),
                            'jobs': jobs})


## Delete Cycle View, redirects to Manage Cycles View ##
def delete_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    cycle.delete()
    messages.success(request, 'Cycle deleted.',
                    extra_tags='manage_cycle')
    
    return redirect(reverse('manage_cycles', kwargs={'username':username}))

## Mark a Cycle as cancelled but don't delete ##
## If Re-instated, see if Each Cycle was Previously Approved ##
## and Set Status to Pending if this is the case. ##

def cancel_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    status = get_object_or_404(CycleStatus, cycle=cycle)
    if request.POST['cancel'] == 'True':
        status.cancelled = True
        status.pending = False
        status.save(update_fields=['cancelled', 'pending', 'complete'])
    elif request.POST['cancel'] == 'False':
        status.cancelled = False
        status.save(update_fields=['cancelled'])
        CycleStatuses(cycle).set_pending()

    return redirect(reverse('manage_cycles', kwargs={'username':username}))

## Reset Cycle Statuses and Delete Associated Files with that Cycle ##

def reset_cycle(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    clear_status(cycle)
    clear_value(cycle)
    delete_all_files(request, cycle_id)
    messages.success(request,   
                    'Cycle reset',
                    extra_tags='manage_cycle')

    return redirect(reverse('manage_cycles', kwargs={'username':username}))