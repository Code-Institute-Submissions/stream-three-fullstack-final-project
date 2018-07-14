from django.shortcuts import render

# Create your views here.

def porthole(request, username, id):
    return render(request, 'porthole.html')