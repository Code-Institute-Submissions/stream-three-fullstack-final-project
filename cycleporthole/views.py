import datetime
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
from .view_func import GetFile, GetStepStatus, DeleteFile
from notify.notify import NewClient, NewFile, get_email_details
############## VIEWS #################################

## Returns Porthole Template ##
### REFACTOR THIS SO THAT FORM VALIDATION ERRORS APPEAR ##
def porthole(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    profile = get_object_or_404(MemberClient, client=cycle.client.id)
    quote_status = GetStepStatus(cycle).get_quote_status()
    quote_form = QuotesForm()
    po_form = PurchaseOrderForm()
    invoice_form = InvoiceForm()
    
    if request.method == 'POST':
        quote_form = QuotesForm(request.POST, request.FILES)
        if quote_form.is_valid():
            new_quote = Quotes(file=quote_form.cleaned_data['file'],
                                uploaded_at=datetime.datetime.now(),
                                cycle_value=quote_form.cleaned_data['cycle_value'],
                                client=cycle.client,
                                member=cycle.member,
                                cycle=cycle)
            try:
                old_quote = Quotes.objects.get(cycle=cycle)
            except Quotes.DoesNotExist:
                old_quote = None
            if old_quote:
                old_quote.delete()
                new_quote.save()
                print('Old Quote Deleted, New Saved')
            elif not old_quote:
                new_quote.save()
                print('Quote Saved')
        
            return redirect(reverse('porthole', kwargs={'username':username,
                                                        'cycle_id':cycle_id,
                                                        'client_username': client_username}))
    context = {'member': cycle.member,
                'client': cycle.client,
                'client_profile': profile,
                'quote_form': quote_form,
                'po_form': po_form,
                'invoice_form':invoice_form,
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

## Called when a file is uploaded and redirected to Porthole View ##
#def upload(request, username, cycle_id, client_username, step):
   # cycle = get_object_or_404(Cycles, pk=cycle_id)                      
    #if request.method == 'POST':
      #  upload = UploadFile(request, 
      #              cycle.client, 
      #              cycle.member, 
       #             cycle)
       # if step == 'quote':
            
        #    upload.upload_quote()
        #elif step == 'po':
         #     upload.upload_po()
        #elif step == 'invoice':
         #   upload.upload_invoice()
        
       # return redirect(reverse('porthole',
        #                            kwargs={'username':username,
         #                               'cycle_id': cycle.id,
          #                              'client_username':client_username,
           #                             }))

## Send Email Notification of Quote Upload and redirect to Porthole View ##
def step_notify(request, username, cycle_id, client_username, step):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    kwargs = get_email_details(username, client_username)
    kwargs['cycle'] = cycle
    #print(step)
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

"""
### REFACTOR THIS SO THAT FORM VALIDATION ERRORS APPEAR ##
def porthole(request, username, cycle_id, client_username):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    profile = get_object_or_404(MemberClient, client=cycle.client.id)
    quote_status = GetStepStatus(cycle).get_quote_status()

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

## Called when a file is uploaded and redirected to Porthole View ##
def upload(request, username, cycle_id, client_username, step):
    cycle = get_object_or_404(Cycles, pk=cycle_id)                      
    if request.method == 'POST':
        upload = UploadFile(request, 
                    cycle.client, 
                    cycle.member, 
                    cycle)
        if step == 'quote':
            upload.upload_quote()
        elif step == 'po':
              upload.upload_po()
        elif step == 'invoice':
            upload.upload_invoice()
        
        return redirect(reverse('porthole',
                                    kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        'client_username':client_username,
                                        }))

## Send Email Notification of Quote Upload and redirect to Porthole View ##
def step_notify(request, username, cycle_id, client_username, step):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    kwargs = get_email_details(username, client_username)
    kwargs['cycle'] = cycle
    print(step)
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

    
"""
    
