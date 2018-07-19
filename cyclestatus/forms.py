from django import forms
from django.forms import ModelForm
from .models import QuoteStatus, POStatus, InvoicesStatus


class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=[('approve','Approve'), ('contest', 'Contest')],
                                 widget=forms.RadioSelect, label='Approve or Contest.')
    comment = forms.CharField(required=False, max_length=150, 
                                widget=forms.Textarea,  
                                label="Leave a comment")

class UrgentForm(forms.Form):
    urgent = forms.ChoiceField(required=True, 
                                choices=[('flag', 'Flag'),('unflag', 'Unflag')],
                                widget=forms.RadioSelect, 
                                label='Flag upload as Urgent')

class ActionForm(forms.Form):
    action_required = forms.ChoiceField(required=True,
                                        choices=[('action_required', 'Action'),
                                                    ('no_action', 'No Action')],
                                        widget=forms.RadioSelect,
                                        label='Action Required')