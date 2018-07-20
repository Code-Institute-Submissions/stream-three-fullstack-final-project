from django.shortcuts import render

# Create your views here.
def manage_account(request, username):
    return render(request, 'manage.html', {'username': username})