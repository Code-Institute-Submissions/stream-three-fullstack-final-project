import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles
from accounts.models import AllUser
from cyclestatus.models import CycleStatus
from manageclient.models import MemberClient
from .upload import UploadFile
from .view_func import GetFile, CycleStatuses, DeleteFile, get_porthole_context
from notify.notify import NewClient, NewFile, get_email_details

############## VIEWS #################################

## Returns Porthole Template ##
def porthole(request, username, cycle_id, client_username):
    CycleStatuses(cycle_id).set_pending() ## Set Pending Payment Status ##
    context = get_porthole_context(cycle_id) ## Get Context ##
    quote_form = QuotesForm()
    po_form = PurchaseOrderForm()
    invoice_form = InvoiceForm()
    if request.method == 'POST':
        upload = UploadFile(context['client'], 
                            context['member'], 
                            context['cycle'])
        if request.POST.get('step_type') == 'quote':
            quote_form = QuotesForm(request.POST, request.FILES)
            if quote_form.is_valid():
                upload.upload_quote(quote_form)
                cycle = get_object_or_404(Cycles, pk=cycle_id)
                cycle.cycle_value = quote_form.cleaned_data.get('cycle_value')
                cycle.save(update_fields=['cycle_value'])
        elif request.POST.get('step_type') == 'po':
            po_form = PurchaseOrderForm(request.POST, request.FILES)
            if po_form.is_valid():
                upload.upload_po(po_form)
        elif request.POST.get('step_type') == 'invoice':
            invoice_form = InvoiceForm(request.POST, request.FILES)
            if invoice_form.is_valid():
                upload.upload_invoice(invoice_form)
        return redirect(reverse('porthole', kwargs={'username':username,
                                                    'cycle_id':cycle_id,
                                                    'client_username': client_username}))                                                          
    return render(request, 'porthole.html', {'context':context,
                                            'quote_form': quote_form,
                                            'po_form': po_form,
                                            'invoice_form':invoice_form})

## Send Email Notification of Quote Upload and redirect to Porthole View ##
def step_notify(request, username, cycle_id, client_username, step):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    kwargs = get_email_details(username, client_username)
    kwargs['cycle'] = cycle
    if step == 'quote':
        NewFile(**kwargs).new_quote_notification()
    elif step == 'po':
        NewFile(**kwargs).new_po_notification()
    elif step == 'invoice':
        NewFile(**kwargs).new_invoice_notification()

    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        'client_username':client_username,
                                        }))

## Delete File and Redirect to Porthole ##
def delete_file(request, username, cycle_id, client_username, step):
    if step == 'quote':
        DeleteFile(request, cycle_id).delete_quote()
    elif step == 'po':
        DeleteFile(request, cycle_id).delete_po()
    elif step =='invoice':
        DeleteFile(request, cycle_id).delete_invoice()
        
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

