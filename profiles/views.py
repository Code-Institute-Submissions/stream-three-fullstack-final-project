from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
from .view_func import profile_exists, edit_profile, new_profile
from accounts.models import AllUser
from django.shortcuts import render, get_object_or_404

# Create your views here.


    
def member_profile(request, username):
    """ Create New Profile or Edit Member Profile if Existing """
    profile = ProfileForm()
    user = get_object_or_404(AllUser, username=username)
    user_id = user.pk
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            is_existing = profile_exists(user_id)
            if is_existing:
                edit_profile(profile, is_existing)
                messages.success(request,'You have edited your profile.')
                return redirect(reverse('member_profile', kwargs={'username':username}))
            else:
                new_profile(profile, user)
                messages.success(request,'You have created your profile.')
                return redirect(reverse('member_profile', kwargs={'username':username}))
    
    return render(request, 'member_profile.html', {'username':username, 
                                                    'profile_form':profile})