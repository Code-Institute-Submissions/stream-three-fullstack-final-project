from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import JobsForm
from accounts.forms import AllUser
from .models import Jobs
# Create your views here.

## Helper Functions ##

def get_all_jobs_for_user(username, user_id):
    try:
        jobs = Jobs.objects.filter(member=user_id)
    except Jobs.DoesNotExist:
        jobs = None
    return jobs

## Return new Job Form and All Current Jobs for User ##

def manage_jobs(request, username):
    user_id = get_object_or_404(AllUser, username=username).pk
    jobs = get_all_jobs_for_user(username, user_id)
    #form = JobsForm(user_id)
    if request.method == 'POST':
        member = get_object_or_404(AllUser, username=username)
        user_id = member.pk
        job_form = JobsForm(user_id, request.POST)
        if job_form.is_valid():
            print('valid')
            client = get_object_or_404(AllUser, 
                                        username=job_form.cleaned_data.get('client'))
            new_job = Jobs(job_title=job_form.cleaned_data.get('job_title'),
                            job_number=job_form.cleaned_data.get('job_number'),
                            location=job_form.cleaned_data.get('location'),
                            start_date=job_form.cleaned_data.get('start_date'),
                            end_date=job_form.cleaned_data.get('start_date'),
                            member=member,
                            client=client)
            new_job.save()
            messages.success = (request, 'New Job Created.')
            return redirect(reverse('manage_jobs', 
                                    kwargs={'username':username}))
    else:
        form = JobsForm(user_id)
        return render(request, 'manage_jobs.html', {'username':username,
                                                    'form':form,
                                                    'jobs':jobs })

## Create Job View, Redirect to Manage_Jobs ##

#def create_job(request, username):
    
## Edit Job View, Redirect to Manage Jobs ##

## Delete Job View, Redirect to Manage Jobs ##
def delete_job(request, username, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Jobs, pk=job_id)
        job.delete()
        return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))