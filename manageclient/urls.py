from django.conf.urls import url, include
from .views import manage_clients

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/manage_clients$', manage_clients, name='manage_clients'),
    
]