from django.shortcuts import render, get_object_or_404
from .forms import CycleForm
from .models import Cycles      
from accounts.models import AllUser
from manageclient.models import MemberClient 

# Create your views here.

# FUNCTIONS #

# GET ALL CLIENTS FOR GIVEN USER #
def get_clients_of_member(user_id):
    try:
        clients = MemberClient.objects.filter(member=user_id)
    except MemberClient.DoesNotExist:
        clients = None
    return clients

def member_cycles(request, username):
    
    user_id = get_object_or_404(AllUser, username=username).pk
    cycle_form = CycleForm(user_id)
    # GET ALL CLIENTS #

    clients = MemberClient.objects.filter(member=user_id)
    for item in clients:
        print(item.member)

    if request.method == 'POST':
        new_form = CycleForm(request.POST)
        #if new_form.is_valid():
           # new_cycle = Cycles(job_title=new_form.cleaned_data['job_title'],
                                #location=new_form.cleaned_data['location'],
                               # description=new_form.cleaned_data['description'],
                                #member=user_id)
            #new_cycle.save()

        
    #username = request.session['user']
    return render(request, 'member_cycles.html', 
                            {'username':username,
                            'cycle_form':cycle_form})

def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
