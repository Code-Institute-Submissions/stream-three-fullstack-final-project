from django.shortcuts import render

# Create your views here.

def manage_clients(request):
    return render(request, 'manage_clients')