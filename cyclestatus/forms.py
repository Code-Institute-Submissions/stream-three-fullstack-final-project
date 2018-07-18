from django import forms
from django.forms import ModelForm
from .models import QuoteStatus, POStatus, InvoicesStatus

class QuoteStatusForm(ModelForm):


    class Meta:
        model = QuoteStatus
        fields = ['approve', 'contest', 'comment']

class POStatusForm(ModelForm):
    
    class Meta:
        model = POStatus
        fields = ['approve', 'contest', 'comment']

class InvoicesStatusForm(ModelForm):
    
    class Meta:
        model = InvoicesStatus
        fields = ['approve', 'contest', 'comment']