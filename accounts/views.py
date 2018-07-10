import os
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from accounts.forms import UserLoginForm
from .forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import AllUser
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def index(request):
    """Returns Index.html or redirects to Profiles"""
    """If already logged in redirect to relevant profile"""
    if request.user.is_authenticated:
        if request.user.is_member:
            return redirect(reverse('member_cycles', kwargs={'username':request.user.username}))
        elif request.user.is_client:
            return redirect(reverse('client_cycles', kwargs={'username':request.user.username}))
    
    subject = 'notification'
    html_message = render_to_string('../templates/emails/client_account_email.html')
    plain_message = strip_tags(html_message)
    from_email = os.environ.get('EMAIL_ADDRESS')
    to = ['dafydd_archard@hotmail.com']
    send_mail(subject, plain_message, from_email, to, html_message=html_message,fail_silently=True)
    
    
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
    """ Register a New Member """
    register = UserRegisterForm()
    if request.user.is_authenticated:
        return redirect(reverse('member_cycles', kwargs={'username':request.user.username}))
        
    if request.method == 'POST':
        register = UserRegisterForm(request.POST)
        if register.is_valid():
            AllUser.objects.create_user(first_name=register.cleaned_data['first_name'],
                                        last_name=register.cleaned_data['last_name'],
                                        company=register.cleaned_data['company'],
                                        phone=register.cleaned_data['phone'],
                                        position=register.cleaned_data['position'],
                                        username=register.cleaned_data['username'],
                                        email=register.cleaned_data['email'],
                                        password=register.cleaned_data['password1'],
                                        is_member=True,
                                        is_client=False
                                        )

            messages.success(request, "You have successfully created an account! Please go back to the login page and login.")
            
    else:
        register = UserRegisterForm()
    return render(request, 'register.html', {'register': register})