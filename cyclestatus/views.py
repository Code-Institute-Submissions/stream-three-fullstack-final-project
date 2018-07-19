from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .models import Quotes, PurchaseOrder, Invoices
from cycles.models import Cycles
from accounts.models import AllUser
from cyclestatus.models import QuoteStatus, POStatus, InvoicesStatus
from cyclestatus.models import QuoteUrgency, POUrgency, InvoiceUrgency
from cyclestatus.forms import StatusForm, UrgentForm

## Helper Function to Views ##
def set_status(status_form):
    """Set Status to Bool"""
    if status_form.is_valid():
        if status_form.cleaned_data['status'] == 'approve':
            approve = True
            contest = False
        elif status_form.cleaned_data['status'] == 'contest':
            approve = False
            contest = True
        comment = status_form.cleaned_data['comment']

        return approve, contest, comment

def set_urgency(form):
    """Set Urgency to Bool"""

    if form.is_valid():
        if form.cleaned_data['urgent'] == 'flag':
            flag = True
        elif form.cleaned_data['urgent'] == 'unflag':
            flag = False

        return flag


## Set Status of Quote ##
def set_quote_status(request, username, cycle_id, client_username):
    """Get Quote by Cycle Id, Save form to Model and Redirect back to Porthole"""
    try:
        quote = Quotes.objects.get(cycle=cycle_id)
    except Quotes.DoesNotExist:
        messages.error(request, "A quote needs to be uploaded before you can set a status.")
        quote = None
    #quote = get_object_or_404(Quotes,cycle=cycle_id)
    if quote != None:
        if request.method == 'POST':
            status_form = StatusForm(request.POST)
            status = QuoteStatus(approve=set_status(status_form)[0],
                                contest=set_status(status_form)[1], 
                                comment=set_status(status_form)[2],
                                quote=quote)
            status.save()
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))


## Set Urgency of Quote ##
def set_quote_urgency(request, username, cycle_id, client_username):
    """ Set Urgency of Quote, save to Model and Redirect to Porthole """
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    if request.method == 'POST':
        form = UrgentForm(request.POST)
        urgency = set_urgency(form)
        quote_urgency = QuoteUrgency(urgent=urgency,
                                    cycle=cycle)
        quote_urgency.save()
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

## Set Status of PO ##
def set_po_status(request, username, cycle_id, client_username):
    """Get PO by Cycle Id, Save form to Model and Redirect back to Porthole"""
    try:
        po = PurchaseOrder.objects.get(cycle=cycle_id)
    except PurchaseOrder.DoesNotExist:
        messages.error(request, "A PO needs to be uploaded before you can set a status.")
        po = None
    #po = get_object_or_404(PurchaseOrder,cycle=cycle_id)
    if po != None:
        if request.method == 'POST':
            status_form = StatusForm(request.POST)
            status = POStatus(approve=set_status(status_form)[0],
                                contest=set_status(status_form)[1], 
                                comment=set_status(status_form)[2],
                                po=po)
            status.save()
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

def set_po_urgency(request, username, cycle_id, client_username):
    """ Set Urgency of PO, save to Model and Redirect to Porthole """
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    if request.method == 'POST':
        form = UrgentForm(request.POST)
        urgency = set_urgency(form)
        po_urgency = POUrgency(urgent=urgency,
                                cycle=cycle)
        po_urgency.save()
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

## Set Status of Invoice ##
def set_invoice_status(request, username, cycle_id, client_username):
    """Get Invoice by Cycle Id, Save form to Model and Redirect back to Porthole"""
    try:
        invoice = Invoices.objects.get(cycle=cycle_id)
    except Invoices.DoesNotExist:
        messages.error(request, "An Invoice needs to be uploaded before you can set a status.")
        invoice = None
    #invoice = get_object_or_404(Invoices, cycle=cycle_id)
    if invoice != None:
        if request.method == 'POST':
            status_form = StatusForm(request.POST)
            status = InvoicesStatus(approve=set_status(status_form)[0],
                                contest=set_status(status_form)[1], 
                                comment=set_status(status_form)[2],
                                invoice=invoice)
            status.save()
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))
    return redirect(reverse('porthole', 
                            kwargs={'username':username,
                                    'cycle_id': cycle_id,
                                    'client_username':client_username,
                                    }))


def set_invoice_urgency(request, username, cycle_id, client_username):
    """ Set Urgency of Invoice, save to Model and Redirect to Porthole """
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    if request.method == 'POST':
        form = UrgentForm(request.POST)
        urgency = set_urgency(form)
        invoice_urgency = InvoiceUrgency(urgent=urgency,
                                    cycle=cycle)
        invoice_urgency.save()
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))