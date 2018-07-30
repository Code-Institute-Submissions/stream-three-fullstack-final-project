from django.shortcuts import render
from .models import Payment, PaymentLineItem
from .forms import PaymentForm


# Create your views here.
def payment(request, username, client_username, cycle_id):
    payment = PaymentForm()
    return render(request, 'payment.html', {'payment_form': payment })