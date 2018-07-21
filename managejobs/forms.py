from django import forms
from .models import Jobs
from django.core.exceptions import ValidationError
from manageclient.models import MemberClient

## Form for New Job Creation, with Dynamically Attachable Client ##
class JobsForm(forms.Form):
        
    def __init__(self, user_id, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.client_choices = MemberClient.objects.filter(member=self.user_id)
        self.fields['job_title'] = forms.CharField(max_length=50)
        self.fields['job_number'] = forms.CharField(max_length=20)
        self.fields['location'] = forms.CharField(max_length=150,
                                                    widget=forms.Textarea)
        self.fields['start_date'] = forms.DateField(widget=forms.SelectDateWidget)
        self.fields['end_date'] = forms.DateField(widget=forms.SelectDateWidget)
        self.fields['client'] = forms.ModelChoiceField(queryset=self.client_choices, 
                                                        label='Attach Client',
                                                        initial=0)

    def clean_job_number(self):

        form_job_number = self.cleaned_data.get('job_number')
        try:
            existing_jobs = Jobs.objects.filter(
                                        member=self.user_id
                                        ).filter(
                                        job_number=form_job_number   
                                        )
            print(existing_jobs)
        except Jobs.DoesNotExist:
            existing_jobs = None

        if existing_jobs:
            raise ValidationError(u'The job number already exists. Make it is unique.')
      
        return form_job_number
        