from django import forms
from .models import Cycles
from manageclient.models import MemberClient 
from accounts.models import AllUser


class CycleForm(forms.Form):
    
    def __init__(self, user_id):
        self.user_id = user_id


    job_title = forms.CharField(max_length = 50)
    location = forms.CharField(max_length=50)
    description = forms.CharField(max_length=150, 
                                    widget=forms.Textarea)
    client = forms.ChoiceField(label='Attach Client',
                                queryset=MemberClient.objects.filter(self.user_id))
    
    class Meta:
        model = Cycles
        fields = ['job_title', 'location', 'description']   