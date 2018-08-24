from django.shortcuts import get_object_or_404
from .models import Jobs
from managecycle.models import Cycles
from manageclient.models import MemberClient
from accounts.models import AllUser

## Helper Functions for Manage Jobs views ##

## Get a QuerySet of all of the Users Jobs ##
def get_all_jobs_for_user(user_id):
    try:
        jobs = Jobs.objects.filter(member=user_id).order_by('job_title')
    except Jobs.DoesNotExist:
        jobs = None
    return jobs

## Establish if the User has clients. Needed in order to ##
## flag in manage_clients template whether a user needs to create ##
## a client before creating a job. ##
def does_the_user_have_clients(username, user_id):
    try:
       clients = MemberClient.objects.filter(member=user_id)
    except MemberClient.DoesNotExist:
        clients = None
    return clients

## Create Job Helper Function ## 
def create_job(form, member):
    client = get_object_or_404(AllUser, 
                                username=form.cleaned_data.get('client'))
    new_job = Jobs(job_title=form.cleaned_data.get('job_title'),
                    job_number=form.cleaned_data.get('job_number'),
                    member=member,
                    client=client)
    new_job.save()
    return True

## Update Client field of Cycle Model when Job Client changes ##
#def update_cycles_client(job, client):
 #   try:
  #      cycles = Cycles.objects.filter(job=job)
   # except Cycles.DoesNotExist:
    #    cycles = None

    #if cycles:
     #   for cycle in cycles:
      #      cycle.client = client
       #     cycle.save(update_fields=['client'])
    
   #     return True

## Update the selected Job, preserving Job Number ##
def update_job(job, form, client):
    job.job_title = form.cleaned_data.get('job_title')
    job.client = client
    job.save(update_fields=['job_title', 'client']) 
    return True
