from django import forms
from .models import Jobs
from django.shortcuts import get_object_or_404
from accounts.models import AllUser
from django.core.exceptions import ValidationError
from manageclient.models import MemberClient

## Abstract Form for New Job Creation, with Dynamically Attachable Client ##
class ParentJobForm(forms.Form):
    def __init__(self, user_id, *args, **kwargs):
        super(ParentJobForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.client_choices = MemberClient.objects.filter(member=self.user_id)
        self.fields['job_title'] = forms.CharField(max_length=50, 
                                                    label="",
                                                    widget=forms.TextInput(
                                                    attrs={'placeholder':'Job Name',}
                                                    ))
        self.fields['client'] = forms.ModelChoiceField(queryset=self.client_choices,
                                                        to_field_name='client',
                                                        label="")
        self.fields['client'].empty_label = "Attach a client"

## Inherits from Parent Job Form with added Job Number Field, contains Clean Method ##
class JobsForm(ParentJobForm):

    def __init__(self, user_id, *args, **kwargs):
        super(JobsForm, self).__init__(user_id, *args, **kwargs) 
        self.fields['job_number'] = forms.CharField(max_length=20, label="",
                                                    widget=forms.TextInput(
                                                    attrs={'placeholder':'Job Number'}
                                                    ))

    def clean_job_number(self):
        form_job_number = self.cleaned_data.get('job_number')
        user = get_object_or_404(AllUser, pk=self.user_id)
       
        try:
            existing_jobs = Jobs.objects.filter(
                                        member=user
                                        ).filter(
                                        job_number=form_job_number   
                                        )  
        except Jobs.DoesNotExist:
            
            existing_jobs = None
             
        if existing_jobs:
            raise forms.ValidationError(u'Job number already exists for your company.')
        else:
            print(form_job_number)
            return form_job_number

## Inherits from Parent Job Form with Job Number field in READ ONLY, clean Method removed. ##
## This allows the Job to be edited preserving the Job Number, and stops clean job number Validation 
## message being triggered. ##

class EditJobsForm(ParentJobForm):
    def __init__(self, user_id, *args, **kwargs):
        super(EditJobsForm, self).__init__(user_id, *args, **kwargs) 
        self.fields['job_number'] = forms.CharField(
                                    widget=forms.TextInput(attrs={'readonly':'readonly'}),
                                    max_length=20, label="")
        
    
    