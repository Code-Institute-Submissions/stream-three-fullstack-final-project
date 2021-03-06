from django.contrib import messages
from django.shortcuts import get_object_or_404
from .models import Profile
from manageclient.models import MemberClient

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
    is_existing.address1 = profile.cleaned_data['address1']
    is_existing.address2 = profile.cleaned_data['address2']
    is_existing.city = profile.cleaned_data['city']
    is_existing.region = profile.cleaned_data['region']
    is_existing.post_code = profile.cleaned_data['post_code']
    is_existing.country = profile.cleaned_data['country']
    is_existing.position = profile.cleaned_data['position']
    is_existing.save()
    return True
    
        
## Create a New Profile ##
def new_profile(profile, user):
    new_profile = Profile(company=profile.cleaned_data['company'],
                            phone=profile.cleaned_data['phone'],
                            address1=profile.cleaned_data['address1'],
                            address2=profile.cleaned_data['address2'],
                            city=profile.cleaned_data['city'],
                            region=profile.cleaned_data['region'],
                            post_code=profile.cleaned_data['post_code'],
                            position=profile.cleaned_data['position'],
                            country = profile.cleaned_data['country'],
                            user=user)
    new_profile.save()
    return True

## Get Profile based on client id, write to Profile model ##
def add_profile_in_member_client_model(client_id):
    profile = get_object_or_404(Profile, user=client_id)
    add_profile = get_object_or_404(MemberClient, client=client_id)
    add_profile.profile = profile
    add_profile.save()
    return True
