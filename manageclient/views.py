from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from accounts.models import AllUser
from profiles.models import Profile
from profiles.view_func import profile_exists
from .models import MemberClient
from .view_func import email_client_account_details, create_client
from accounts.forms import UserRegisterForm
from accounts.notify import NotifyClient

def manage_clients(request, username):
    """Create New Client and Write to MemberClient Model keys of Member and Client"""
    new_client = UserRegisterForm()
    if request.method == "POST":
        new_client = UserRegisterForm(request.POST)
        user_id = get_object_or_404(AllUser, username=username).pk
        profile = profile_exists(user_id)
        if profile:
            if new_client.is_valid():
                client_created = create_client(username, new_client)
                if client_created:
                    email_client_account_details(profile, username, new_client) 
                    messages.success(request, "You have successfully created a new client!")       
        # ELSE MESSAGE SAYING COMPLETE PROFILE BEFORE YOU CAN CREATE AN ACCOUNT #
        else:
            messages.error(request, "You need to complete your profile before you can create a client account.")
            return render(request, 'manage_clients.html', {'new_client': new_client, 'username':username})

    return render(request, 'manage_clients.html', {'new_client': new_client, 'username':username})