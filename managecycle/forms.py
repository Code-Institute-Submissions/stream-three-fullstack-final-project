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
        self.fields['cycle_title'] = forms.CharField(max_length=50,
                                                        label="",
                                                        widget=forms.TextInput(
                                                        attrs={'class':'register-form__input',
                                                        'placeholder':'Cycle Name'}))
        self.fields['description'] = forms.CharField(max_length=150,
                                                    label="",
                                                    widget=forms.Textarea(
                                                        attrs={'class':'manage__cycle-text-field',
                                                        'placeholder':'Description'}))
        self.fields['location'] = forms.CharField(max_length=50,
                                                    label="",
                                                    widget=forms.TextInput(
                                                    attrs={'class':'register-form__input',
                                                    'placeholder':'Location'}))                                   
        self.fields['start_date'] = forms.DateField(widget=forms.SelectDateWidget(
                                                        attrs={'label':''}))                                        
        self.fields['end_date'] = forms.DateField(widget=forms.SelectDateWidget(
                                                         attrs={'label':''}))
        self.fields['jobs'] = forms.ModelChoiceField(queryset=self.job_choices,
                                                    label="")
        self.fields['jobs'].empty_label='Attach a Job'

                                 