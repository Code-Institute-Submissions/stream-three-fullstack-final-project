from django.shortcuts import render, get_object_or_404
from .forms import QuotesForm
from .models import Quotes
from cycles.models import Cycles
from accounts.models import AllUser

## Need to Upload Media to Dynamic Folder ##
## Need to Retrieve Project Name and Details ##
## Need to Retrieve Status of Each Cycle Stage ##
## for logic in showing next stage Divs ##

def porthole(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    member = get_object_or_404(AllUser, username=username)
    client = get_object_or_404(AllUser, username=client_username)
    quote_form = QuotesForm()
    if request.method == 'POST':
        quote_form = QuotesForm(request.POST, request.FILES)
        #print('valid')
        if quote_form.is_valid():
            new_quote = Quotes(file=quote_form.cleaned_data['file'],
                                cycle_value=quote_form.cleaned_data['cycle_value'],
                                client=client,
                                member=member,
                                cycle=cycle)
            new_quote.save()

    context = {'username': username,
                'client': client,
                'cycle_id': cycle_id, 
                'form': quote_form,
                'cycle': cycle}

    return render(request, 'porthole.html', {'context':context})