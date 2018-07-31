from django.shortcuts import get_object_or_404
from .forms import CycleForm
from .models import Cycles      
from accounts.models import AllUser
from managejobs.models import Jobs
from cyclestatus.models import CycleStatus
from cycleporthole.view_func import DeleteFile

## Helper Functions for Views ##

##  Creates New Cycle, Called By Member Cycle View ##
## Get Job Object from Job Table, Get Client from Job Table ##
def create_cycle(user_id, request, user):
    new_form = CycleForm(user_id, request)
    if new_form.is_valid():
        job = new_form.cleaned_data.get('jobs')
        client = get_object_or_404(Jobs, pk=job.id).client
        new_cycle = Cycles(cycle_title=new_form.cleaned_data.get('cycle_title'),
                           description=new_form.cleaned_data.get('description'),
                           location=new_form.cleaned_data.get('location'),
                           start_date=new_form.cleaned_data.get('start_date'),
                           end_date=new_form.cleaned_data.get('end_date'),
                            member=user,
                            client=client,
                            job=job)
        new_cycle.save()
        return True
    else:
        return False

## Get all User Cycles ##
def get_user_cycles(user):
    try:
        users_cycles = CycleStatus.objects.filter(
                                                cycle__member=user
                                                ).order_by('cycle__job__job_title')
    except Cycles.DoesNotExist:
        users_cycles = None
    return users_cycles

## Update Cycle ##
def update_cycle(cycle, form, request):
    cycle.cycle_title = form.cleaned_data.get('cycle_title')
    cycle.description = form.cleaned_data.get('description')  
    cycle.location = form.cleaned_data.get('location')
    cycle.start_date = form.cleaned_data.get('start_date')
    cycle.end_date = form.cleaned_data.get('end_date')
    cycle.jobs = form.cleaned_data.get('jobs')
    cycle.save(update_fields=['cycle_title', 'description', 'location',
                                'start_date', 'end_date', 'job'])
    return True

## Resets all Statuses for a Cycle ##
def clear_status(cycle):
    status = get_object_or_404(CycleStatus, cycle=cycle)
    status.approve_quote = False
    status.contest_quote = False
    status.approve_po = False
    status.contest_po = False
    status.approve_invoice = False
    status.contest_invoice = False
    status.complete = False
    status.pending = False
    status.cancelled = False
    status.save() ## Signal listening to the Save of this Model will reset 
    return True

## Deletes all files associated with a Status ##
def delete_all_files(request, cycle_id):
    delete_files = DeleteFile(request, cycle_id)
    delete_files.delete_quote()
    delete_files.delete_po() 
    delete_files.delete_invoice()
    return True