from django import forms
from django.forms import ModelForm
from .models import Cycles
from manageclient.models import MemberClient 
from accounts.models import AllUser
from managejobs.models import Jobs

## FORM RENDERING DYNAMIC CHOICE SELECTION FOR ATTACHING CLIENT TO CYCLE ##
#class CycleForm(forms.Form):
    
    #def __init__(self, user_id, *args, **kwargs):
       # super(CycleForm, self).__init__(*args, **kwargs)
       # self.user_id = user_id
       # self.job_choices = Jobs.objects.filter(member=self.user_id)
       # self.fields['cycle_title'] = forms.CharField(max_length=50)
       # self.fields['description'] = forms.CharField(max_length=150,
       #                                             widget=forms.Textarea)
        #self.fields['jobs'] = forms.ModelChoiceField(queryset=self.job_choices,
                                                  #  label='Attach Job',
                                                  #  initial=0)

   
    