from django.conf.urls import url
from .views import manage_clients

urlpatterns = [

    url(r'^manage_clients/(?P<username>[\w.@+-]+)$', manage_clients, name='manage_clients'),
    
]