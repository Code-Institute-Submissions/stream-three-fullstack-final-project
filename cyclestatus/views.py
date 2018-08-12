from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from cycleporthole.models import Quotes, PurchaseOrder, Invoices
from cyclestatus.models import CycleStatus
from cyclestatus.forms import StatusForm
from .view_func import set_status, email_status

######################## QUOTES VIEWS ###########################################

## Set Status of Quote ##
## Get Quote by Cycle Id, Save form to Model and Redirect back to Porthole ##
def set_quote_status(request, username, cycle_id):
    try:
        quote = Quotes.objects.get(cycle=cycle_id)
    except Quotes.DoesNotExist:
        messages.error(request, 
                        "A quote needs to be uploaded before you can set a status.",
                        extra_tags='quote_message')
        quote = None
    if quote != None:
        if request.method == 'POST':
            status = get_object_or_404(CycleStatus, cycle=quote.cycle)
            status_form = StatusForm(request.POST)
            status.approve_quote = set_status(status_form)[0]
            status.contest_quote = set_status(status_form)[1] 
            status.save(update_fields=['approve_quote', 
                                        'contest_quote'])
            email_status(username, quote.cycle.client.username, cycle_id, 
                         status_form, 'quote')
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        }))
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        }))

######################## PO VIEWS ###########################################

## Set Status of PO ##
## Get PO by Cycle Id, Save form to Model and Redirect back to Porthole ##
def set_po_status(request, username, cycle_id):
    try:
        po = PurchaseOrder.objects.get(cycle=cycle_id)
    except PurchaseOrder.DoesNotExist:
        messages.error(request, 
                        "A PO needs to be uploaded before you can set a status.",
                        extra_tags='po_message')
        po = None
    if po != None:
        if request.method == 'POST':
            status = get_object_or_404(CycleStatus, cycle=po.cycle)
            status_form = StatusForm(request.POST)
            status.approve_po = set_status(status_form)[0]
            status.contest_po = set_status(status_form)[1] 
            status.save(update_fields=['approve_po', 
                                        'contest_po'])
            email_status(username, po.cycle.client.username, cycle_id, 
                         status_form, 'po')
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id
                                        }))
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id
                                        }))

######################## INVOICE VIEWS ###########################################

## Set Status of Invoice ##
## Get Invoice by Cycle Id, Save form to Model and Redirect back to Porthole ##
def set_invoice_status(request, username, cycle_id):
    print('here');
    try:
        invoice = Invoices.objects.get(cycle=cycle_id)
    except Invoices.DoesNotExist:
        messages.error(request, 
                        "An Invoice needs to be uploaded before you can set a status.",
                        extra_tags='invoice_message')
        invoice = None
    if invoice != None:
        if request.method == 'POST':
            status = get_object_or_404(CycleStatus, cycle=invoice.cycle)
            status_form = StatusForm(request.POST)
            status.approve_invoice = set_status(status_form)[0]
            status.contest_invoice = set_status(status_form)[1] 
            status.save(update_fields=['approve_invoice', 
                                        'contest_invoice'])
            email_status(username, invoice.cycle.client.username, cycle_id, 
                         status_form, 'invoice')
            return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id
                                        }))
    return redirect(reverse('porthole', 
                            kwargs={'username':username,
                                    'cycle_id': cycle_id
                                    }))
