from django.contrib import messages
from .models import Profile

## Check if a User already has a Profile ##
def profile_exists(user_id):
    try:
        profile_exists = Profile.objects.get(user=user_id)
    except Profile.DoesNotExist:
        profile_exists = None
    return profile_exists

## Edit Existing Profile ##
def edit_profile(profile, is_existing):
    is_existing.company = profile.cleaned_data['company']
    is_existing.phone = profile.cleaned_data['phone']
    is_existing.position = profile.cleaned_data['position']
    is_existing.save()
    return True
    
        
## Create a New Profile ##
def new_profile(profile, user):
    new_profile = Profile(company=profile.cleaned_data['company'],
                            phone=profile.cleaned_data['phone'],
                            position=profile.cleaned_data['position'],
                            user=user)
    new_profile.save()
    return True