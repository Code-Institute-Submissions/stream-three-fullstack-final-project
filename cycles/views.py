from django.shortcuts import render

# Create your views here.

def member_cycles(request, username):
    
    #username = request.session['user']
    return render(request, 'member_cycles.html', {'username':username})

def client_cycles(request, username):
    
    return render(request, 'client_cycles.html', {'username':username})
