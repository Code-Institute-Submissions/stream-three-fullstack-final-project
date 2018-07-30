from django.conf.urls import url
from .views import payment

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', payment, name='payment'),
]