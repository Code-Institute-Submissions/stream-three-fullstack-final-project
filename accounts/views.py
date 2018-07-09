from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import AllUser

def index(request):
    """Returns Index.html or redirects to Profiles"""
    """If already logged in redirect to relevant profile"""
    if request.user.is_authenticated:
        if request.user.is_member:
            return redirect(reverse('member_cycles', kwargs={'username':request.user.username}))
        elif request.user.is_client:
            return redirect(reverse('client_cycles', kwargs={'username':request.user.username}))
    
    """If POST authenticate User"""
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
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

def register(request):
    register = UserRegisterForm()
    if request.method == 'POST':
        register = UserRegisterForm(request.POST)
        if register.is_valid():
            first_name = register.cleaned_data['first_name']
            last_name = register.cleaned_data['last_name']
            company = register.cleaned_data['company']
            phone = register.cleaned_data['phone']
            username = register.cleaned_data['username']
            email = register.cleaned_data['email']
            password1 = register.cleaned_data['password1']
            password2 = register.cleaned_data['password2']
            print(password1)
            #new_user = AllUser(first_name=first_name,
                                #last_name=last_name,
                                #company=company,
                                #phone=phone,
                                #username=username,
                                #email=email,
                                #password1=password1,
                                #password2=password2)
            AllUser.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        company=company,
                                        phone=phone,
                                        username=username,
                                        email=email,
                                        password=password1
                                        )
            #print(first_name)
    else:
        register = UserRegisterForm()
    return render(request, 'register.html', {'register': register})