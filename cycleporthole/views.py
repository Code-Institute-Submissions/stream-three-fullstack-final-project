from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
from cycles.models import Cycles
from accounts.models import AllUser
from .upload import UploadFile
from .view_func import get_porthole_info


## Need to Upload Media to Dynamic Folder ##
## Need to Retrieve Project Name and Details ##
## Need to Retrieve Status of Each Cycle Stage ##
## for logic in showing next stage Divs ##


############## VIEWS #################################

## Returns Cycle Detailed Information including upload forms ##
def porthole(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, 
                            client_username)
    quote_form = QuotesForm()
    po_form = PurchaseOrderForm()
    invoice_form = InvoiceForm()
    context = {'username': username,
                'client': info['client'],
                'cycle_id': cycle_id, 
                'quote_form': quote_form,
                'po_form': po_form,
                'invoice_form':invoice_form,
                'cycle': info['cycle']}

    return render(request, 'porthole.html', {'context':context})

## Called When a Quote is uploaded and redirected to Porthole View ##
def quote_upload(request, username, cycle_id, client_username):
    info = get_porthole_info(username, cycle_id, 
                            client_username)
    if request.method == 'POST':
        print(request)
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
    print('here')
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