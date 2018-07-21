from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from accounts.models import AllUser
from profiles.models import Profile
from profiles.view_func import profile_exists
from .models import MemberClient
from .view_func import email_client_account_details, create_client
from .view_func import get_all_clients_of_user
from accounts.forms import UserRegisterForm
from accounts.notify import NotifyClient

## Create New Client and Write pk of Member and Client to MemberClient Model ##
def manage_clients(request, username):
    user_id = get_object_or_404(AllUser, username=username).pk
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
                    email_client_account_details(profile, username, new_client) 
                    messages.success(request, "You have successfully created a new client, they have been emailed their credentials!")
                    return redirect(reverse('manage_clients', kwargs={'username':username}))      
        else:
            messages.error(request, "You need to complete your profile before you can create a client account.")
            return render(request, 'manage_clients.html', {'new_client': new_client, 
                                                            'username':username,
                                                            'clients':clients_exist})

    return render(request, 'manage_clients.html', {'new_client': new_client, 
                                                    'username':username,
                                                    'clients':clients_exist})

## Delete Client from AllUser Model ##
def delete_client(request, username, client_id):
    client = get_object_or_404(AllUser, pk=client_id)
    client.delete()
    return redirect(reverse('manage_clients', kwargs={'username': username}))

