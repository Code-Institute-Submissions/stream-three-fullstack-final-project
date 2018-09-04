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
    jobs = get_all_jobs_for_user(user_id)
    clients = does_the_user_have_clients(username, user_id)
    form = JobsForm(user_id)
    if request.method == 'POST':
        if 'update' in request.POST.keys(): 
            job = get_object_or_404(Jobs, pk=(int(request.POST['job_id'])))
            request.session['update_job_id'] = job.id
            form = EditJobsForm(request.user, model_to_dict(job))
        else:
            if 'updated' in request.POST.keys():
                form = EditJobsForm(request.user, request.POST)
                if form.is_valid():
                    client = get_object_or_404(AllUser, 
                                                username=form.cleaned_data.get('client'))
                    job = get_object_or_404(Jobs, 
                                            pk=request.session['update_job_id'])
                    update_job(job, form)
                    messages.success(request, 'Job updated.')
                    return redirect(reverse('manage_jobs',
                                                kwargs={'username':username})) 
            else:
                form = JobsForm(user_id, request.POST)
                if form.is_valid():
                    create_job(form, request.user)
                    messages.success(request, 'Job Created.')
                    return redirect(reverse('manage_jobs',
                                                kwargs={'username':username})) 

    return render(request, 'manage_jobs.html', {'username':username,
                                                'form':form,
                                                'jobs':jobs,
                                                'clients':clients })


## Delete Job View, Redirect to Manage Jobs ##
def delete_job(request, username, job_id):

    if request.method == 'POST':
        job = get_object_or_404(Jobs, pk=job_id)
       
        job.delete()
        messages.success(request, 'Job deleted.',
                        fail_silently=True)
        return redirect(reverse('manage_jobs',
                                kwargs={'username':username}))