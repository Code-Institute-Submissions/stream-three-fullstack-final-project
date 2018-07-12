from django import forms
from .models import Cycles
from manageclient.models import MemberClient 
from accounts.models import AllUser

## FORM RENDERING DYNAMIC CHOICE SELECTION FOR ATTACHING CLIENT TO CYCLE ##
class CycleForm(forms.Form):
    
    def __init__(self, user_id, *args, **kwargs):
        super(CycleForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.choices = MemberClient.objects.filter(member=self.user_id)
        self.fields['job_title'] = forms.CharField(max_length=50)
        self.fields['location'] = forms.CharField(max_length=50)
        self.fields['description'] = forms.CharField(max_length=150,
                                                    widget=forms.Textarea)
        self.fields['clients'] = forms.ModelChoiceField(queryset=self.choices, 
                                                        label='Attach Client',
                                                        initial=0)
   
