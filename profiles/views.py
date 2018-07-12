from django.shortcuts import render
from django.contrib import messages
from .models import Profile
from .forms import ProfileForm
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
            try:
                profile_exists = Profile.objects.get(user=user_id)
            except Profile.DoesNotExist:
                profile_exists = None
            if profile_exists:
                profile_exists.company = profile.cleaned_data['company']
                profile_exists.phone = profile.cleaned_data['phone']
                profile_exists.position = profile.cleaned_data['position']
                profile_exists.save()
                messages.success(request,'You have edited your profile.')
            else:
                new_profile = Profile(company=profile.cleaned_data['company'],
                                        phone=profile.cleaned_data['phone'],
                                        position=profile.cleaned_data['position'],
                                        user=user)
                new_profile.save()

                messages.success(request,'You have edited your profile.')
    
    return render(request, 'member_profile.html', {'username':username, 
                                                    'profile_form':profile})