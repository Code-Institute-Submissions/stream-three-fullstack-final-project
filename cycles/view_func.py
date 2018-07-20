from django.contrib import messages
from managecycle.forms import CycleForm
from managecycle.models import Cycles      
from accounts.models import AllUser

##  Creates New Cycle, Called By Member Cycle View ##
def create_cycle(user_id, request, user):
    new_form = CycleForm(user_id, request)
    if new_form.is_valid():
        client_user = new_form.cleaned_data.get('clients')
        client_object = AllUser.objects.get(username=client_user)
        new_cycle = Cycles(job_title=new_form.cleaned_data.get('job_title'),
                            location=new_form.cleaned_data.get('location'),
                            description=new_form.cleaned_data.get('description'),
                            member=user,
                            client=client_object)
        new_cycle.save()
        return True
    else:
        return False

def get_user_cycles(user):
    try:
        users_cycles = Cycles.objects.filter(member=user)
    except Cycles.DoesNotExist:
        users_cycles = None
    return users_cycles