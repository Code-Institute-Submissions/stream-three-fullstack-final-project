from django import forms
from django.forms import ModelForm
from .models import Cycles
from manageclient.models import MemberClient 
from accounts.models import AllUser
from managejobs.models import Jobs


class CycleForm(forms.Form):
    
    def __init__(self, member, *args, **kwargs):
        super(CycleForm, self).__init__(*args, **kwargs)
        self.member = member
        self.job_choices = Jobs.objects.filter(member=self.member)
        #print(self.job_choices)
        self.fields['cycle_title'] = forms.CharField(max_length=50)
        self.fields['description'] = forms.CharField(max_length=150,
                                                    widget=forms.Textarea)
        self.fields['jobs'] = forms.ModelChoiceField(queryset=self.job_choices,
                                                    label='Attach Job',
                                                    initial=0)