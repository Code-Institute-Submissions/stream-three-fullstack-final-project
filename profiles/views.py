from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.forms.models import model_to_dict
from .models import Profile
from .forms import ProfileForm
from .view_func import profile_exists, edit_profile, new_profile
from .view_func import add_profile_in_member_client_model
from accounts.models import AllUser
from django.shortcuts import render, get_object_or_404

## View to Create a Full Member Profile ##
def member_profile(request, username):
    user = request.user
    user_id = user.pk
    is_existing = profile_exists(user_id)
    if is_existing:
        profile = ProfileForm(model_to_dict(is_existing))
    else:
        profile = ProfileForm()
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            if is_existing:
                edit_profile(profile, is_existing)
                messages.success(request, 'Profile updated.')
                return redirect(reverse('member_profile', kwargs={'username':username}))
            else:
                new_profile(profile, user)
                messages.success(request, 'Profile created.')
                return redirect(reverse('member_profile', kwargs={'username':username}))
    
    return render(request, 'member_profile.html', {'username':username, 
                                                    'profile_form':profile,
                                                    'existing':is_existing})

## View to Create or Edit Client Profile ##
def client_profile(request, username, client_id):
    client = get_object_or_404(AllUser, pk=client_id)
    is_existing = profile_exists(client_id)
    if is_existing:
        profile = ProfileForm(model_to_dict(is_existing))
    else:
        profile = ProfileForm() 
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            if is_existing:
                edit_profile(profile, is_existing)
                add_profile_in_member_client_model(client_id)
                messages.success(request, 'Profile updated.')
                return redirect(reverse('client_profile', kwargs={'username':username,
                                                                    'client_id':client_id}))

            else:
                new_profile(profile, client)
                add_profile_in_member_client_model(client_id)
                messages.success(request, 'Profile created.')
                return redirect(reverse('client_profile', kwargs={'username':username,
                                                                    'client_id':client_id}))
    return render(request, 'client_profile.html', {'username':username,
                                                    'profile_form':profile,
                                                    'client':client,
                                                    'existing':is_existing})