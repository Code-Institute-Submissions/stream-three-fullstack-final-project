import os
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags


class NotifyClient:
    """Class Sends emails to clients"""
    def __init__(self, recipient_email, 
                recipient_name, 
                sender_name, 
                company,
                client_username
                ):
        self.recipient_email = recipient_email
        self.recipient_name = recipient_name
        self.sender_name = sender_name
        self.company = company
        self.client_username = client_username
        
    def client_user_created(self):
        subject = 'New Client Account at Fileo.'
        html_message = render_to_string('../templates/emails/client_account_email.html',
                                        {'recipient_email':self.recipient_email,
                                            'recipient_name' : self.recipient_name,
                                            'sender_name': self.sender_name,
                                            'company': self.company,
                                            'client_username':self.client_username })
        plain_message = strip_tags(html_message)
        from_email = os.environ.get('EMAIL_ADDRESS')
        to = [self.recipient_email]
        send_mail(subject, plain_message, from_email, to, html_message=html_message,fail_silently=True)


class NotifyMember():
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
