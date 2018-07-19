from django import forms
from .models import Jobs
from manageclient import MemberClient

class JobsForm(forms.Form):
        
    def __init__(self, user_id, *args, **kwargs):
        super(JobsForm, self).__init__(*args, **kwargs)
        self.user_id = user_id
        self.client_choices = MemberClient.objects.filter(member=self.user_id)
        self.fields['cycle_title'] = forms.CharField(max_length=50)
        self.fields['description'] = forms.CharField(max_length=150,
                                                    widget=forms.Textarea)
        self.fields['clients'] = forms.ModelChoiceField(queryset=self.client_choices, 
                                                        label='Attach Client',
                                                        initial=0)
