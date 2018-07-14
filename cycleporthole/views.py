from django.shortcuts import render
from .forms import QuotesForm
from .models import Quotes


def porthole(request, username, cycle_id, client):
    new_form = QuotesForm()

    context = {'username': username,
                'client': client,
                'cycle_id': cycle_id,
                'form':new_form}

    return render(request, 'porthole.html', {'context':context})