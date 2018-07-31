from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Order, OrderLineItem
from .forms import OrderForm, PaymentForm
from managecycle.views import Cycles
from profiles.models import Profile
from profiles.view_func import profile_exists

# Create your views here.
def payment(request, username, cycle_id):
    total = get_object_or_404(Cycles, pk=cycle_id).cycle_value
    profile = profile_exists(request.user.pk)
    order = OrderForm()
    payment = PaymentForm()
    if profile:
        profile_dict = model_to_dict(profile)
        name = '{0} {1}'.format(request.user.first_name, request.user.last_name)
        profile_dict['name_on_card'] = name
        order = OrderForm(profile_dict)
    else:
        order = OrderForm()
    return render(request, 
                'payment.html', 
                {'order_form': order,
                'payment_form': payment,
                'total': total })