from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Quotes, PurchaseOrder, Invoices
from cycles.models import Cycles
from accounts.models import AllUser
from cyclestatus.models import QuoteStatus


def set_quote_status(request, username, cycle_id, client_username):
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))