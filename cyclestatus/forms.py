from django import forms
from django.forms import ModelForm

## STATUS FORM FOR EACH CYCLE STEP ##
## ALLOWS USER TO APPROVE OR CONTEST A STEP ##
class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=[('approve','Approve'), ('contest', 'Contest')],
                                 widget=forms.RadioSelect, label='')
    

