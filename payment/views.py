from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .models import Order, OrderLineItem
from cyclestatus.models import CycleStatus
from .forms import OrderForm, PaymentForm
from managecycle.views import Cycles
from profiles.models import Profile
from profiles.view_func import profile_exists
import stripe
from fileo import settings

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
    

@login_required
def payment(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    total = cycle.cycle_value
    stripe_total = convert_total_for_stripe(total)
    profile = profile_exists(request.user.pk)
    order_form = OrderForm()
    payment_form = PaymentForm()
    if profile:
        profile_dict = model_to_dict(profile)
        name = '{0} {1}'.format(request.user.first_name, request.user.last_name)
        profile_dict['name_on_card'] = name
        order_form = OrderForm(profile_dict)
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        payment_form = PaymentForm(request.POST)
        print(payment_form)
        if order_form.is_valid() and payment_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            line_item = OrderLineItem(order=order,
                                    cycle=cycle)
            line_item.save()
            print('here')
            try:
                customer = stripe.Charge.create(
                    amount=stripe_total,
                    currency = 'GBP',
                    description = request.user.email,
                    card = payment_form.cleaned_data['stripe_id']
                )
                print('charge')
            except stripe.error.CardError:
                messages.error(request,
                                'Card Error. Check your details and try again.')
                print('error')
           
            if customer.paid:
                messages.success(request, 'Payment Successful. This Cycle is now Complete.')
                cycle_status = get_object_or_404(CycleStatus, pk=cycle_id)
                cycle_status.pending = False
                cycle_status.cancelled = False
                cycle_status.complete = True
                cycle_status.save(update_fields=['pending', 'cancelled', 'complete'])

            else:
                messages.error(request, 'Apologies, we could not take payment with that card.')

    return render(request, 
                    'payment.html', 
                    {'order_form': order_form,
                    'payment_form': payment_form,
                    'publishable': settings.STRIPE_PUBLISHABLE,
                    'total': total })

