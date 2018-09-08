import stripe
from django.utils import timezone
from fileo import settings
from django.contrib import messages
from django.shortcuts import get_object_or_404
from cyclestatus.models import CycleStatus


stripe.api_key = settings.STRIPE_SECRET

## Helper Functions/Classes ##

## Convert Total Django-Money Object to int ##
def convert_total_for_stripe(total):
    stripe_total = str(total).split(' ')
    stripe_total = stripe_total[0].split(',')
    stripe_total = ''.join(stripe_total).split('.')
    stripe_total = ''.join(stripe_total)
    stripe_total = stripe_total.split('£')
    stripe_total = int(''.join(stripe_total))
    return stripe_total

## Save Order Form to Order Model ##    
def save_order(cycle, order_form):
    order = order_form.save(commit=False)
    order.cycle = cycle
    order.save()
    return True

## Create Stripe Charge ##
def create_payment(request, cycle, payment_form, stripe_total):
    print(payment_form.cleaned_data['stripe_id'])
    try:
        customer = stripe.Charge.create(
            amount=stripe_total,
            currency = 'GBP',
            description = cycle.id,
            card = payment_form.cleaned_data['stripe_id']
        )
    except stripe.error.CardError:
        messages.error(request,
                        'Card Error. Check your details and try again.',
                        fail_silently=True)  
    return customer

## Set Cycle Status to Complete ##
def set_status_to_complete(cycle):
    cycle_status = get_object_or_404(CycleStatus, cycle=cycle)
    cycle_status.pending = False
    cycle_status.cancelled = False
    cycle_status.complete = True
    cycle_status.save(update_fields=['pending', 'cancelled', 'complete'])
    return True

