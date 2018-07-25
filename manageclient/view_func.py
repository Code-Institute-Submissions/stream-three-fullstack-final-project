from django.shortcuts import get_object_or_404
from accounts.models import AllUser
from profiles.models import Profile
from profiles.view_func import profile_exists
from .models import MemberClient
from notify.notify import NotifyClient

## Create New Client and Client Member Relationship ##  
def create_client(username, new_client):
        AllUser.objects.create_user(first_name=new_client.cleaned_data['first_name'],
                                    last_name=new_client.cleaned_data['last_name'],
                                    username=new_client.cleaned_data['username'],
                                    email=new_client.cleaned_data['email'],
                                    password=new_client.cleaned_data['password1'],
                                    is_member=False,
                                    is_client=True
                                    )
        member = get_object_or_404(AllUser, username=username)
        client = get_object_or_404(AllUser, username=new_client.cleaned_data['username'])
        if member and client:
            new_member_client = MemberClient(client=client, member=member)
            new_member_client.save()
            return True

## Email Client Account Details ##
#def email_client_account_details(profile, username, new_client):
   # client_username = new_client.cleaned_data['username']
   # member = get_object_or_404(AllUser, username=username)
   # client = get_object_or_404(AllUser, username=client_username)
   # new_email = NotifyClient(client.email,
                                  #  client.first_name, 
                                  #  member.first_name,
                                 #   client.username,
                                  #  profile.company
                                  #  )
    #new_email.client_user_created()
   # return True

def get_all_clients_of_user(user_id):
    try: 
        clients = MemberClient.objects.filter(member=user_id)
        count = MemberClient.objects.filter(member=user_id).count   
    except MemberClient.DoesNotExist:
        clients = None
    
    return clients, count

