from django.shortcuts import render, get_object_or_404
from django.forms.models import model_to_dict
from .models import Payment, PaymentLineItem
from .forms import PaymentForm
from managecycle.views import Cycles
from profiles.models import Profile
from profiles.view_func import profile_exists

# Create your views here.
def payment(request, username, cycle_id):
    total = get_object_or_404(Cycles, pk=cycle_id).cycle_value
    profile = profile_exists(request.user.pk)
    if profile:
        profile_dict = model_to_dict(profile)
        name = '{0} {1}'.format(request.user.first_name, request.user.last_name)
        profile_dict['name_on_card'] = name
        payment = PaymentForm(profile_dict)
    else:
        payment = PaymentForm(profile_dict)
    return render(request, 
                'payment.html', 
                {'payment_form': payment,
                'total': total })