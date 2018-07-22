from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import FormView
from django.contrib import messages
from django.forms.models import model_to_dict
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
## GET JOB BY JOB ID AND POPULATE FORM, REDIRECT TO EDIT JOB WITH SUCCESSFULLY EDITED MESSAGE ##
def edit_job(request, username, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    user_id = get_object_or_404(AllUser, username=username)
    form = JobsForm(user_id, model_to_dict(job))

    return render(request, 'edit_job.html', {'username':username,
                                            'form': form,
                                            'job': job })

## Delete Job View, Redirect to Manage Jobs ##
def delete_job(request, username, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Jobs, pk=job_id)
        job.delete()
        return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))