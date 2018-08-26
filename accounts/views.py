from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import AllUser
from notify.notify import NewMember


## Returns Index.html or redirects to Profiles ## 
## If already logged in redirect to relevant Account ## 
def index(request):
    if request.user.is_authenticated:
        if request.user.is_member:
            return redirect(reverse('member_cycles', kwargs={'username':request.user.username}))
        elif request.user.is_client:
            return redirect(reverse('client_cycles', kwargs={'username':request.user.username}))
    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)
        if login_form.is_valid():
            user = auth.authenticate(request, username=request.POST['username'], 
                                        password=request.POST['password'])
            if user:
                if user.is_member:
                    auth.login(user=user, request=request)
                    return redirect(reverse('member_cycles', kwargs={'username':user.username}))
                elif user.is_client:
                    auth.login(user=user, request=request)
                    return redirect(reverse('client_cycles', kwargs={'username': user.username}))
            else:
                messages.error(request, "Oops! We couldn't find you. Try again.")
    else: 
        login_form = UserLoginForm()
    return render(request, 'index.html', {'login_form':login_form})

## LOGOUT ##
@login_required
def logout(request):
    auth.logout(request)
    messages.success(request, "You have been logged out of Fileo.")
    return redirect(reverse('index'))

## REGISTER A NEW MEMBER ACCOUNT ##
def register(request):
    register = UserRegisterForm()
    if request.user.is_authenticated:
        return redirect(reverse('member_cycles', kwargs={'username':request.user.username})) 
    if request.method == 'POST':
        register = UserRegisterForm(request.POST)
        if register.is_valid():
            AllUser.objects.create_user(first_name=register.cleaned_data['first_name'],
                                        last_name=register.cleaned_data['last_name'],
                                        username=register.cleaned_data['username'],
                                        email=register.cleaned_data['email'],
                                        password=register.cleaned_data['password1'],
                                        is_member=True,
                                        is_client=False
                                        )
            messages.success(request, 
                            """Account created.""")
            new_email = NewMember(register.cleaned_data['first_name'],
                                register.cleaned_data['email'], 
                                register.cleaned_data['username'],
                                )
            new_email.member_created()
            return redirect(reverse('register'))

    return render(request, 'register.html', {'register': register})