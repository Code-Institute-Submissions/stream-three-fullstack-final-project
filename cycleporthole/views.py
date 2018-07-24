from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
from .models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles
from accounts.models import AllUser
from cyclestatus.models import QuoteStatus
from cyclestatus.forms import StatusForm
from manageclient.models import MemberClient
from .upload import UploadFile
from .view_func import GetFile, GetStepStatus
############## VIEWS #################################

## Returns Porthole Template ##
def porthole(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    profile = get_object_or_404(MemberClient, client=cycle.client.id)
    quote_status = GetStepStatus(cycle).get_quote_status()
    #print(quote_status.approve)
    
    context = {'member': cycle.member,
                'client': cycle.client,
                'client_profile': profile,
                'quote_form': QuotesForm(),
                'po_form': PurchaseOrderForm(),
                'invoice_form':InvoiceForm(),
                'status_form':StatusForm(),
                'cycle': cycle,
                'quote': GetFile(cycle).get_quote(),
                'po': GetFile(cycle).get_po(),
                'invoice': GetFile(cycle).get_invoice(),
                'quote_status': quote_status,
                'po_status': GetStepStatus(cycle).get_po_status(),
                'invoice_status': GetStepStatus(cycle).get_invoice_status()
                 }

    return render(request, 'porthole.html', {'context':context})

## Called When a Quote is uploaded and redirected to Porthole View ##
def quote_upload(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
                            
    if request.method == 'POST':
        UploadFile(request, 
                    cycle.client, 
                    cycle.member, 
                    cycle).upload_quote()
        return redirect(reverse('porthole',
                                 kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        'client_username':client_username,
                                        }))

## Called When a PO is uploaded and redirected to Porthole View ##
def po_upload(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
                            
    if request.method == 'POST':
        UploadFile(request, 
                    cycle.client, 
                    cycle.member, 
                    cycle).upload_po()
        return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        'client_username':client_username,
                                        }))

## Called When an Invoice is uploaded and redirected to Porthole View ##
def invoice_upload(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
                            
    if request.method == 'POST':
        UploadFile(request, 
                    cycle.client, 
                    cycle.member,
                    cycle).upload_invoice()
        return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        'client_username':client_username,
                                        }))

def delete_quote(request, username, cycle_id, client_username):

    quote = Quotes.objects.get(cycle=cycle_id)
    quote.delete()
    messages.success(request, 'You successfully deleted your quote.')
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id,
                                        'client_username':client_username,
                                        }))
