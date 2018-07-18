from django import forms
from django.forms import ModelForm
from .models import QuoteStatus, POStatus, InvoicesStatus


class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=[('approve','Approve'), ('contest', 'Contest')],
                                 widget=forms.RadioSelect, label='Status')
    comment = forms.CharField(required=False, max_length=150, 
                                widget=forms.Textarea, 
                                label="Leave a comment")

