from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from accounts.models import AllUser
from .models import MemberClient
from accounts.forms import UserRegisterForm
from accounts.notify import NotifyClient

# Create your views here.

def manage_clients(request, username):
    """Create New Client and Write to MemberClient Model keys of Member and Client"""
    new_client = UserRegisterForm()
    if request.method == "POST":
        new_client = UserRegisterForm(request.POST)
        if new_client.is_valid():
            client_username = new_client.cleaned_data['username']
            AllUser.objects.create_user(first_name=new_client.cleaned_data['first_name'],
                                        last_name=new_client.cleaned_data['last_name'],
                                        company=new_client.cleaned_data['company'],
                                        phone=new_client.cleaned_data['phone'],
                                        position=new_client.cleaned_data['position'],
                                        username=new_client.cleaned_data['username'],
                                        email=new_client.cleaned_data['email'],
                                        password=new_client.cleaned_data['password1'],
                                        is_member=False,
                                        is_client=True
                                        )
            member = get_object_or_404(AllUser, username=username)
            client = get_object_or_404(AllUser, username=client_username)
            if member and client:
                new_member_client = MemberClient(client=client, member=member)
                new_member_client.save()
                
            messages.success(request, "You have successfully created a new client!")

            new_email = NotifyMember(client.email,
                                client.first_name, 
                                member.first_name,
                                member.company,
                                client.username
                                )
            new_email.client_user_created()

    return render(request, 'manage_clients.html', {'new_client': new_client, 'username':username})