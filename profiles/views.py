from django.shortcuts import render
from .models import Profile
from .forms import ProfileForm
from accounts.models import AllUser
from django.shortcuts import render, get_object_or_404

# Create your views here.
def member_profile(request, username):
    """ Create New Profile or Edit Member Profile if Existing """
    profile = ProfileForm()
    user_id = get_object_or_404(AllUser, username=username).pk
    if request.method == 'POST':
        profile = ProfileForm(request.POST)
        if profile.is_valid():
            existing_profile = get_object_or_404(Profile, user=user_id)
            if existing_profile:
                existing_profile.company = profile.cleaned_data['company']
                existing_profile.phone = profile.cleaned_data['phone']
                existing_profile.position = profile.cleaned_data['position']
                existing_profile.save()
            else:
                user = get_object_or_404(AllUser, username=username)
                new_profile = Profile(company=profile.cleaned_data['company'],
                                        phone=profile.cleaned_data['phone'],
                                        position=profile.cleaned_data['position'],
                                        user=user)
                new_profile.save()
        

    return render(request, 'member_profile.html', {'username':username, 
                                                    'profile_form':profile})