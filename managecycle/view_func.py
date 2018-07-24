from django.shortcuts import get_object_or_404
from .forms import CycleForm
from .models import Cycles      
from accounts.models import AllUser
from managejobs.models import Jobs

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
        users_cycles = Cycles.objects.filter(member=user)
        count = Cycles.objects.filter(member=user).count()
    except Cycles.DoesNotExist:
        users_cycles = None
    return users_cycles, count

def update_cycle(cycle,form):
    cycle.cycle_title = form.cleaned_data.get('cycle_title')
    cycle.description = form.cleaned_data.get('description')
    cycle.location = form.cleaned_data.get('location'),
    cycle.start_date = form.cleaned_data.get('start_date'),
    cycle.end_date = form.cleaned_data.get('end_date'),
    cycle.jobs = form.cleaned_data.get('jobs')
    cycle.cancelled = form.cleaned_data.get('cancelled')
    cycle.save()
    return True