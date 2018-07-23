from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic import FormView
from django.contrib import messages
from django.forms.models import model_to_dict
from .forms import JobsForm, EditJobsForm
from accounts.forms import AllUser
from .models import Jobs
from .view_func import get_all_jobs_for_user, does_the_user_have_clients
from .view_func import create_job, update_job
## Return Manage Jobs Template ##
## User can see all jobs and create new ones ##
def manage_jobs(request, username):
    member = get_object_or_404(AllUser, username=username)
    user_id = member.id
    jobs = get_all_jobs_for_user(username, user_id)
    clients = does_the_user_have_clients(username, user_id)
    form = JobsForm(user_id)
    if request.method == 'POST':
        form = JobsForm(user_id, request.POST)
        if form.is_valid():
            job_created = create_job(form, member)
            if job_created:
                messages.success(request, 'New Job Created.')
                return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))          
    return render(request, 'manage_jobs.html', {'username':username,
                                                'form':form,
                                                'jobs':jobs[0],
                                                'jobs_count': jobs[1],
                                                'clients':clients })

    
## Edit Job View, Redirect to Manage Jobs ##
def edit_job(request, username, job_id):
    job = get_object_or_404(Jobs, pk=job_id)
    user_id = get_object_or_404(AllUser, username=username)
    form = EditJobsForm(user_id, model_to_dict(job))
    if request.method == 'POST':
        form = EditJobsForm(user_id, request.POST)
        if form.is_valid():
            job_updated = update_job(job, form)
            if job_updated:
                messages.success(request, 'You have successfully edited Job No: {0}'.format(
                                                            form.cleaned_data.get('job_number')
                                                        ))
                return redirect(reverse('manage_jobs', kwargs={'username':username}))
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