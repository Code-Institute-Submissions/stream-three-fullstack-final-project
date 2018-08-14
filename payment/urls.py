from django.conf.urls import url
from .views import payment#, payment_success

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)$', payment, name='payment'),
    #url(r'^(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/payment-success$', payment_success, name='payment_success')
]