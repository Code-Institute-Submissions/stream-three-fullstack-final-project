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
        print(step)
    return redirect(reverse('porthole',
                                kwargs={'username':username,
                                    'cycle_id': cycle.id,
                                    'client_username':client_username,
                                    }))


## Called When a PO is uploaded and redirected to Porthole View ##
#def po_upload(request, username, cycle_id, client_username):
   # cycle = get_object_or_404(Cycles, pk=cycle_id)
                            
   # if request.method == 'POST':
       # UploadFile(request, 
                  #  cycle.client, 
                   # cycle.member, 
                    #cycle).upload_po()
        
       # return redirect(reverse('porthole', 
        #                        kwargs={'username':username,
         #                               'cycle_id': cycle.id,
          #                              'client_username':client_username,
           #                             }))

## Called When an Invoice is uploaded and redirected to Porthole View ##
#def invoice_upload(request, username, cycle_id, client_username):
 #   cycle = get_object_or_404(Cycles, pk=cycle_id)
                            
  #  if request.method == 'POST':
   #     UploadFile(request, 
    #                cycle.client, 
     #               cycle.member,
      #              cycle).upload_invoice()            
       # return redirect(reverse('porthole', 
        #                        kwargs={'username':username,
         #                               'cycle_id': cycle.id,
          #                              'client_username':client_username,
           #                             }))

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


    

## Delete PO and Redirect to Porthole ##
#def delete_po(request, username, cycle_id, client_username):
#    po = GetFile(cycle_id).get_po()
#    if po:
#        po.delete()
#        messages.success(request, 
#                        'You successfully deleted your Purchase Order.',
#                        extra_tags='po_delete')
#    else:
#        messages.error(request, 
#                        "You haven't uploaded a file yet. There is nothing to delete.",
#                        extra_tags='po_delete')
#    return redirect(reverse('porthole', 
#                                        'cycle_id': cycle_id,
#                                        'client_username':client_username,
#                                        }))
###                                kwargs={'username':username,


## Delete Invoice and Redirect to Porthole ##
#def delete_invoice(request, username, cycle_id, client_username):
#    invoice = GetFile(cycle_id).get_invoice()
 #       invoice.delete()
#    if invoice:
#        messages.success(request, 
#                        'You successfully deleted your Invoice.',
 #                       extra_tags='invoice_delete')
#    else:
#        messages.error(request, 
#                        "You haven't uploaded a file yet. There is nothing to delete.",
#                        extra_tags='invoice_delete')
#    return redirect(reverse('porthole', 
#                                kwargs={'username':username,
#                                        'cycle_id': cycle_id,
#                                        'client_username':client_username,
 #                                       }))


    

    
