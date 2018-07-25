import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404
from django.utils.html import strip_tags
from accounts.models import AllUser
from profiles.models import Profile


## Return basic details for formulating an email ##

def get_email_details(username, client_username):
    client = get_object_or_404(AllUser, username=client_username)
    member = get_object_or_404(AllUser, username=username)
    member_profile = get_object_or_404(Profile, user=member)
    details = {'client': client,
                'member': member,
                'member_profile': member_profile}
    return details

class NotifyClient:
    """Class Sends emails to clients"""
    def __init__(self, **kwargs):
        self.client = kwargs.get('client')
        self.member = kwargs.get('member')
        self.profile = kwargs.get('member_profile')
        self.cycle = kwargs.get('cycle')
       

    def client_user_created(self):
        subject = 'New Client Account at Fileo.'
        html_message = render_to_string('../templates/emails/client_account_email.html',
                                        {'recipient_email': self.client.email,
                                        'recipient_name' : self.client.first_name,
                                        'sender_name': self.member.first_name,
                                        'client_username': self.client.username,
                                        'member_company': self.profile.company})
        plain_message = strip_tags(html_message)
        from_email = os.environ.get('EMAIL_ADDRESS')
        to = [self.client.email]
        send_mail(subject, plain_message, from_email, to, 
                    html_message=html_message,fail_silently=True)
        print(self.client.username)

    def new_quote_notification(self):
        subject = 'New Quote in your Client Porthole.'
        html_message = render_to_string('../templates/emails/client_quote_email.html',
                                        {'recipient_email': self.client.email,
                                        'recipient_name' : self.client.first_name,
                                        'sender_name': self.member.first_name,
                                        'client_username': self.client.username,
                                        'member_company': self.profile.company,
                                        'job': self.cycle.job,
                                        'cycle': self.cycle,
                                        'is_quote': True })
        plain_message = strip_tags(html_message)
        from_email = os.environ.get('EMAIL_ADDRESS')
        to = [self.client.email]
        send_mail(subject, plain_message, from_email, to, 
                    html_message=html_message,fail_silently=True)
        


class NotifyMember:
    """Class sends emails to Members"""
    def __init__(self, member_name, member_email, member_username):
        self.member_name = member_name
        self.member_email = member_email
        self.member_username = member_username

    def member_created(self):
        subject = 'New Member Account at Fileo.'
        html_message = render_to_string('../templates/emails/member_account_email.html',
                                        {'member_email':self.member_email,
                                            'member_name' : self.member_name,
                                            'member_username':self.member_username })
        plain_message = strip_tags(html_message)
        from_email = os.environ.get('EMAIL_ADDRESS')
        to = [self.member_email]
        send_mail(subject, plain_message, from_email, to, html_message=html_message,fail_silently=True)
        
    #def send_client_username(self):
