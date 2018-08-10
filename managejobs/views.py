from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.http import Http404
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
## If Updated in POST request run Update Helper instead of Create Helper ##
def manage_jobs(request, username):
    user_id = request.user.id
    jobs = get_all_jobs_for_user(username, user_id)
    clients = does_the_user_have_clients(username, user_id)
    form = JobsForm(user_id)
    if request.method == 'POST':
        if 'update' in request.POST.keys(): ## RENDERS FORM WITH DATA FROM MODEL ##
            job = get_object_or_404(Jobs, pk=(int(request.POST['job_id'])))
            form = EditJobsForm(request.user, model_to_dict(job))
        else:
            if 'updated' in request.POST.keys():
                form = EditJobsForm(request.user, request.POST)
                if form.is_valid():
                    try:
                        job = Jobs.objects.filter(job_number=request.POST['job_number']
                                                    ).filter(member=request.user)
                    except Jobs.DoesNotExist:
                        raise Http404
                    update_job(job[0], form)
                    messages.success(request, 'Job updated.')
            else:
                form = JobsForm(user_id, request.POST)
                if form.is_valid():
                    create_job(form, request.user)
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