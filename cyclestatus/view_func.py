from django.shortcuts import get_object_or_404
from notify.notify import NewStatusNotify, get_email_details
from managecycle.models import Cycles

## Helper Function to Views ##
## Set Status to Bool for writing to Model ##
def set_status(status_form):
    if status_form.is_valid():
        if status_form.cleaned_data['status'] == 'approve':
            approve = True
            contest = False
        elif status_form.cleaned_data['status'] == 'contest':
            approve = False
            contest = True

        return approve, contest

## Set Email Kwargs for status email, and send email to client or member ##
def email_status(username, client_username, 
                cycle_id, status_form, file_type):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    status = set_status(status_form)[0]
   
    ## Set Kwargs ##
    kwargs = get_email_details(username, client_username)
    kwargs['cycle'] = cycle
    if status == True:
        kwargs['status'] = 'Approved'
    else:
        kwargs['status'] = 'Contested'

    ## Set file Key based on view that called it ##
    ## Notify Client or Member dependent on File type ##
    if file_type == 'quote':
        kwargs['file'] = 'Quote'
        NewStatusNotify(**kwargs).status_notify_member()
    elif file_type == 'po':
        kwargs['file'] = 'Purchase Order'
        NewStatusNotify(**kwargs).status_notify_client()
    elif file_type == 'invoice':
        kwargs['file'] = 'Invoice'
        NewStatusNotify(**kwargs).status_notify_member()

    return True