from django.shortcuts import render

# Create your views here.

def cycle_porthole(request):
    return render(request, 'porthole.html')