from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import AllUser

def index(request):
    """Returns Index.html or redirects to Profiles"""
    """If already logged in redirect to relevant profile"""
    #if request.user.is_authenticated:
        #if request.user.is_member:
            #return redirect(reverse('member_cycles', kwargs={'username':request.user.username}))
        #elif request.user.is_client:
            #return redirect(reverse('client_cycles', kwargs={'username':request.user.username}))
    
    """If POST authenticate User"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        print(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request, username=request.POST['username'], 
                                        password=request.POST['password'])
            if user:
                if user.is_member:
                    auth.login(user=user, request=request)
                    messages.success(request, "You have logged in as a member!")
                    return redirect(reverse('member_cycles', kwargs={'username':user.username}))
                elif user.is_client:
                    auth.login(user=user, request=request)
                    messages.success(request, 'You are logged in as client!')
                    return redirect(reverse('client_cycles', kwargs={'username': user.username}))
            else:
                messages.error(request, 'Your credentials are incorrect')
    else: 
        login_form = UserLoginForm()
    return render(request, 'index.html', {'login_form':login_form})

@login_required
def logout(request):
    """Log User Out"""
    #print('logout', request)
    auth.logout(request)
    messages.success(request, "You have been logged out of Fileo.")
    return redirect(reverse('index'))

def member_cycles(request, username):
    """Member Login View"""
    #username = request.session['user']
    return render(request, 'member_cycles.html', {'username':username})

def client_cycles(request, username):
    """Client Login View"""
    return render(request, 'client_cycles.html', {'username':username})