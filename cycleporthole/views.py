from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm
from .models import Quotes
from cycles.models import Cycles
from accounts.models import AllUser


## Need to Upload Media to Dynamic Folder ##
## Need to Retrieve Project Name and Details ##
## Need to Retrieve Status of Each Cycle Stage ##
## for logic in showing next stage Divs ##

    
def upload_quote(request, client, member, cycle):
    quote_form = QuotesForm(request.POST, request.FILES)
    if quote_form.is_valid():
        new_quote = Quotes(file=quote_form.cleaned_data['file'],
                                cycle_value=quote_form.cleaned_data['cycle_value'],
                                client=client,
                                member=member,
                                cycle=cycle)
        try:
            old_quote = Quotes.objects.get(cycle=cycle)
        except Quotes.DoesNotExist:
            old_quote = None
        if old_quote:
            old_quote.delete()
            new_quote.save()
            print('Quote Saved')
        elif not old_quote:
            new_quote.save()
            print('Quote Saved')
            
        return True

## Returns Cycle Detailed Information ##
def porthole(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    member = get_object_or_404(AllUser, username=username)
    client = get_object_or_404(AllUser, username=client_username)
    quote_form = QuotesForm()
    context = {'username': username,
                'client': client,
                'cycle_id': cycle_id, 
                'form': quote_form,
                'cycle': cycle}


    return render(request, 'porthole.html', {'context':context})

## Called When a Quote is uploaded ##
def quote_upload(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    member = get_object_or_404(AllUser, username=username)
    client = get_object_or_404(AllUser, username=client_username)
    if request.method == 'POST':
        upload_quote(request, client, member, cycle)
        return redirect(reverse('porthole', kwargs={'username':username,
                                            'cycle_id': cycle_id,
                                            'client_username':client_username,
                                            }))
