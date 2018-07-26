

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