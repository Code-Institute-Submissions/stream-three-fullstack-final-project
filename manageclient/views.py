from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from accounts.models import AllUser
from profiles.models import Profile
from profiles.view_func import profile_exists
from .models import MemberClient
from .view_func import create_client #email_client_account_details, 
from .view_func import get_all_clients_of_user
from accounts.forms import UserRegisterForm
from notify.notify import NewClient, get_email_details

## Create New Client and Write pk of Member and Client to MemberClient Model ##
def manage_clients(request, username):
    user_id = request.user.pk
    clients_exist = get_all_clients_of_user(user_id)
    new_client = UserRegisterForm()
    if request.method == "POST":
        new_client = UserRegisterForm(request.POST)
        """ Check if a full Profile Exists for User first, force User to create one. """
        profile = profile_exists(user_id)
        if profile:
            if new_client.is_valid():
                client_created = create_client(username, new_client)
                if client_created:
                    client_username = new_client.cleaned_data['username']
                    kwargs = get_email_details(username, 
                                                client_username)

                    NewClient(**kwargs).client_user_created()
                    messages.success(request, 
                                    "Client created and an email has been sent.",
                                    extra_tags="create_client")
                    return redirect(reverse('manage_clients', kwargs={'username':username}))      
        else:
            messages.error(request, 
                            "Profile incomplete. You can't create a client yet.",
                            extra_tags="failed_client")
            return render(request, 'manage_clients.html', {'new_client': new_client, 
                                                            'username':username,
                                                            'clients':clients_exist,
                                                            'clients_count':clients_exist.count()})

    return render(request, 'manage_clients.html', {'new_client': new_client, 
                                                    'username':username,
                                                    'clients':clients_exist,
                                                    'clients_count':clients_exist.count()})

## Delete Client from AllUser Model ##
def delete_client(request, username, client_id):
    client = get_object_or_404(AllUser, pk=client_id)
    #messages.error(request, 
     #               'Are you sure you want to delete this client?',
      #              extra_tags='delete_client')
    print(client)
    if request.method =='POST':
        client.delete()
        messages.success(request, 'Client deleted.')
    return redirect(reverse('manage_clients', kwargs={'username': username}))

