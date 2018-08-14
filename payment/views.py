from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib import messages
from .models import Order
from cyclestatus.models import CycleStatus
from .forms import OrderForm, PaymentForm
from managecycle.views import Cycles
from profiles.models import Profile
from profiles.view_func import profile_exists
from fileo import settings
from .view_func import convert_total_for_stripe, save_order
from .view_func import create_payment, set_status_to_complete
from cycles.view_func import SetSessionValues


## Payment View Populates Order Form with Client Profile information if it exists. ##
## Order is Saved to Order Model, Charge is Created with Stripe and Cycle Status ##
## Updated to COMPLETE if Payment is Completed. On Completion Redirects to Payment ##
## Success View ##.

@login_required
def payment(request, username, cycle_id):
    cycle = get_object_or_404(Cycles, pk=cycle_id)
    status = get_object_or_404(CycleStatus, pk=cycle_id)
    print(status.complete)
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
        if order_form.is_valid() and payment_form.is_valid():
            save_order(cycle, order_form)
            customer = create_payment(request, 
                                        cycle, 
                                        payment_form, 
                                        stripe_total)
            if customer.paid:
                messages.success(request, 'Payment Successful. This Cycle is now Complete.')
                set_status_to_complete(cycle)
                return redirect(reverse('payment', kwargs={'username': username,
                                                                    'cycle_id': cycle_id}))
            else:
                messages.error(request, 'Apologies, we could not take payment with that card.')

    return render(request, 
                    'payment.html', 
                    {'order_form': order_form,
                    'cycle': cycle,
                    'status': status,
                    'payment_form': payment_form,
                    'publishable': settings.STRIPE_PUBLISHABLE,
                    'total': total })
