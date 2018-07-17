from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
from cycles.models import Cycles
from accounts.models import AllUser
from .upload import UploadFile
from .view_func import get_porthole_info

############## VIEWS #################################

## Returns Porthole Template ##
def porthole(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, 
                            client_username)
    context = {'username': username,
                'client': info['client'],
                'cycle_id': cycle_id, 
                'quote_form': QuotesForm(),
                'po_form': PurchaseOrderForm(),
                'invoice_form':InvoiceForm(),
                'cycle': info['cycle'],
                'quote': info['quote'],
                'po': info['po'],
                'invoice': info['invoice']}

    return render(request, 'porthole.html', {'context':context})

## Called When a Quote is uploaded and redirected to Porthole View ##
def quote_upload(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, 
                            client_username)
    if request.method == 'POST':
        UploadFile(request, 
                    info['client'], 
                    info['member'], 
                    info['cycle']).upload_quote()
        return redirect(reverse('porthole',
                                 kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

## Called When a PO is uploaded and redirected to Porthole View ##
def po_upload(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, client_username)
    if request.method == 'POST':
        UploadFile(request, 
                    info['client'], 
                    info['member'], 
                    info['cycle']).upload_po()
        return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))

## Called When an Invoice is uploaded and redirected to Porthole View ##
def invoice_upload(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, 
                            client_username)
    if request.method == 'POST':
        UploadFile(request, 
                    info['client'], 
                    info['member'], 
                    info['cycle']).upload_invoice()
        return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))