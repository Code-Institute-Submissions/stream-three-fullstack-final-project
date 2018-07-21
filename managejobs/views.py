from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import JobsForm
from accounts.forms import AllUser
from .models import Jobs
from .view_func import get_all_jobs_for_user, does_the_user_have_clients

## Return Manage Jobs Template ##
## User can see all jobs and create new ones ##
def manage_jobs(request, username):
    member = get_object_or_404(AllUser, username=username)
    user_id = member.pk
    jobs = get_all_jobs_for_user(username, user_id)
    clients = does_the_user_have_clients(username, user_id)
    form = JobsForm(user_id)
    if request.method == 'POST':
        form = JobsForm(user_id, request.POST)
        if form.is_valid():
            client = get_object_or_404(AllUser, 
                                        username=form.cleaned_data.get('client'))
            new_job = Jobs(job_title=form.cleaned_data.get('job_title'),
                            job_number=form.cleaned_data.get('job_number'),
                            location=form.cleaned_data.get('location'),
                            start_date=form.cleaned_data.get('start_date'),
                            end_date=form.cleaned_data.get('start_date'),
                            member=member,
                            client=client)
            new_job.save()
            messages.success(request, 'New Job Created.')
            return redirect(reverse('manage_jobs', 
                                    kwargs={'username':username}))             
    return render(request, 'manage_jobs.html', {'username':username,
                                                'form':form,
                                                'jobs':jobs,
                                                'clients':clients })

    
## Edit Job View, Redirect to Manage Jobs ##

## Delete Job View, Redirect to Manage Jobs ##
def delete_job(request, username, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Jobs, pk=job_id)
        job.delete()
        return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))