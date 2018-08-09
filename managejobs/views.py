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
## If Update Key in request.POST, render form with inital values ##
def manage_jobs(request, username):
    user_id = request.user.id
    jobs = get_all_jobs_for_user(username, user_id)
    clients = does_the_user_have_clients(username, user_id)
    form = JobsForm(user_id)
    if request.method == 'POST':
        if 'update' in request.POST.keys():
            job = get_object_or_404(Jobs, pk=(int(request.POST['job_id'])))
            form = EditJobsForm(request.user, model_to_dict(job))
        else:
            form = EditJobsForm(request.user, request.POST)
            if form.is_valid():
                job_created = create_job(form, request.user)
                if job_created:
                    if 'updated' in request.POST.keys():
                        messages.success(request, 'Job updated.')
                    else:
                        messages.success(request, 'New Job Created.')
                    return redirect(reverse('manage_jobs',
                                    kwargs={'username':username}))          
    return render(request, 'manage_jobs.html', {'username':username,
                                                'form':form,
                                                'jobs':jobs,
                                                'jobs_count': jobs.count(),
                                                'clients':clients })


## Delete Job View, Redirect to Manage Jobs ##
def delete_job(request, username, job_id):
    if request.method == 'POST':
        job = get_object_or_404(Jobs, pk=job_id)
        job.delete()
        messages.success(request, 'Job deleted.')
        return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))