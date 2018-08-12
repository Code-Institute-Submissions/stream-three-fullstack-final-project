from django import forms
from django.forms import ModelForm

class StatusForm(forms.Form):
    status = forms.ChoiceField(choices=[('approve','Approve'), ('contest', 'Contest')],
                                 widget=forms.RadioSelect, label='')
    #comment = forms.CharField(required=False, max_length=150, 
                               # widget=forms.Textarea,  
                               # label="Leave a comment")

