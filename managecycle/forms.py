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
        print(self.job_choices)
        self.fields['cycle_title'] = forms.CharField(max_length=50)
        self.fields['description'] = forms.CharField(max_length=150,
                                                    widget=forms.Textarea)
        self.fields['location'] = forms.CharField(max_length=150)                                     
        self.fields['start_date'] = forms.DateField(widget=forms.SelectDateWidget)
        self.fields['end_date'] = forms.DateField(widget=forms.SelectDateWidget)
        self.fields['jobs'] = forms.ModelChoiceField(queryset=self.job_choices,
                                                    label='Jobs',
                                                    )
        self.fields['jobs'].empty_label='Attach a Job'

class EditCycleForm(CycleForm):

    def __init__(self, member, *args, **kwargs):
        super(EditCycleForm, self).__init__(member, *args, **kwargs)
        self.choices = (('True', 'Cancel'), ('False', 'Active'))
        self.fields['cancelled'] = forms.ChoiceField(choices=self.choices,
                                                    widget=forms.RadioSelect,
                                                    label='Mark as Cancelled, or still Active.'
                                                    )