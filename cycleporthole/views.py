from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from .forms import QuotesForm, PurchaseOrderForm, InvoiceForm
#from .models import Quotes, PurchaseOrder, Invoices
from managecycle.models import Cycles
#from accounts.models import AllUser
#from cyclestatus.models import CycleStatus
#from manageclient.models import MemberClient
from .upload import UploadFile
from .view_func import GetFile, CycleStatuses, DeleteFile, get_porthole_context
from notify.notify import NewFile, get_email_details #, #NewClient, 
from cycles.view_func import SetSessionValues

############## VIEWS #################################

## Returns Porthole Template ##
def porthole(request, username, cycle_id):
    CycleStatuses(cycle_id).set_pending() ## Sets Pending Payment Status if all steps approved ##
    SetSessionValues(request).set_values()
    context = get_porthole_context(cycle_id) 
    quote_form = QuotesForm()
    po_form = PurchaseOrderForm()
    invoice_form = InvoiceForm()

    if request.method == 'POST': 
        upload = UploadFile(context['client'], 
                            context['member'], 
                            context['cycle'])
        ### DEPENDING ON STEP TYPE, UPLOAD TO RELEVANT MODEL ##
        if request.POST.get('step_type') == 'quote':
            quote_form = QuotesForm(request.POST, request.FILES)
            if quote_form.is_valid():
                upload.upload_quote(quote_form)
                cycle = get_object_or_404(Cycles, pk=cycle_id)
                cycle.cycle_value = quote_form.cleaned_data.get('cycle_value')
                cycle.save(update_fields=['cycle_value'])
                return redirect(reverse('porthole', kwargs={'username':username,
                                                'cycle_id':cycle_id
                                                }))                 
        elif request.POST.get('step_type') == 'po':
            po_form = PurchaseOrderForm(request.POST, request.FILES)
            if po_form.is_valid():
                po_uploaded = upload.upload_po(po_form)
                if not po_uploaded:
                    messages.error(request, 
                                    "You can't upload a PO until there is an approved Quote.",
                                    extra_tags='step2_upload_error')
                return redirect(reverse('porthole', kwargs={'username':username,
                                                'cycle_id':cycle_id
                                                }))        
        elif request.POST.get('step_type') == 'invoice':
            invoice_form = InvoiceForm(request.POST, request.FILES)
            if invoice_form.is_valid():
                invoice_uploaded = upload.upload_invoice(invoice_form)
                if not invoice_uploaded:    
                    messages.error(request, 
                                    "You can't upload an Invoice until there is an approved PO.",
                                    extra_tags='step3_upload_error')
                return redirect(reverse('porthole', kwargs={'username':username,
                                                            'cycle_id':cycle_id
                                                            }))                                                          
    return render(request, 'porthole.html', {'context':context,
                                            'quote_form': quote_form,
                                            'po_form': po_form,
                                            'invoice_form':invoice_form,})


## Send Email Notification of Upload and redirect to Porthole View ##
def step_notify(request, username, cycle_id, step):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    kwargs = get_email_details(username, cycle.client.username)
    kwargs['cycle'] = cycle
    message = 'Notification sent.'
    if step == 'quote':
        NewFile(**kwargs).new_quote_notification()
        messages.success(request, message , extra_tags='quote')
    elif step == 'po':
        NewFile(**kwargs).new_po_notification()
        messages.success(request, message , extra_tags='po')
    elif step == 'invoice':
        NewFile(**kwargs).new_invoice_notification()
        messages.success(request, message , extra_tags='invoice')

    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle.id,
                                        }))

## Delete File and Redirect to Porthole ##
def delete_file(request, username, cycle_id, step):
    if step == 'quote':
        DeleteFile(request, cycle_id).delete_quote()
        cycle = get_object_or_404(Cycles, pk=cycle_id)
        cycle.cycle_value = '0'
        cycle.save(update_fields=['cycle_value'])
    elif step == 'po':
        DeleteFile(request, cycle_id).delete_po()
    elif step =='invoice':
        DeleteFile(request, cycle_id).delete_invoice()
        
    return redirect(reverse('porthole', 
                                kwargs={'username':username,
                                        'cycle_id': cycle_id
                                        }))

