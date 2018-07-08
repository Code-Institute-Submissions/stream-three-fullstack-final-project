from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from django.contrib.auth.decorators import login_required
from .models import AllUser

# Create your views here.

def index(request):
    """Returns Index.html"""
    print('here')
    if request.user.is_authenticated:
        print('user authenticated')
        return redirect(reverse('member_cycles'))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        #print(request.POST['username'])
        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'], 
                                        password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in!")
                print('here')
                return redirect(reverse('member_cycles'))
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

def member_cycles(request):
    """Member Login View"""
    #print(request)
    return render(request, 'member_cycles.html')