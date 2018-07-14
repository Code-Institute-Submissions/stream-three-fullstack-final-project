from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .forms import CycleForm
from .models import Cycles      
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