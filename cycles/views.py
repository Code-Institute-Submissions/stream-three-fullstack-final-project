from django.shortcuts import render, get_object_or_404
from .forms import CycleForm
from .models import Cycles      
from accounts.models import AllUser
from manageclient.models import MemberClient 

# Create your views here.

def member_cycles(request, username):
    user = get_object_or_404(AllUser, username=username)
    user_id = user.pk
    cycle_form = CycleForm(user_id)
    if request.method == 'POST':
        new_form = CycleForm(user_id, request.POST)
        if new_form.is_valid():
            client_user = new_form.cleaned_data.get('clients')
            client_object = AllUser.objects.get(username=client_user)
            print(type(client_object))
            new_cycle = Cycles(job_title=new_form.cleaned_data.get('job_title'),
                                location=new_form.cleaned_data.get('location'),
                                description=new_form.cleaned_data.get('description'),
                                member=user,
                                client=client_object)
            new_cycle.save()
        
    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycle_form':cycle_form})

def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
