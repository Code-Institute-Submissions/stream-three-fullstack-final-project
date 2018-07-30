from django.shortcuts import render

# Create your views here.
def payment(request, username, client_username, cycle_id):
    return render(request, 'payment.html')