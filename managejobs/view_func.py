from .models import Jobs
from manageclient.models import MemberClient

## Helper Functions for Manage Jobs views##

## Get a QuerySet of all of the Users Jobs ##
def get_all_jobs_for_user(username, user_id):
    try:
        jobs = Jobs.objects.filter(member=user_id)
    except Jobs.DoesNotExist:
        jobs = None
    return jobs

## Establish if the User has clients. Needed in order to ##
## flag in the template whether a user needs to create ##
## a client before creating a job. ##
def does_the_user_have_clients(username, user_id):
    try:
       clients = MemberClient.objects.filter(member=user_id)
    except MemberClient.DoesNotExist:
        clients = None
    return clients

