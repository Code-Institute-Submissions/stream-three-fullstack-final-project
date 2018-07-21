from django.conf.urls import url
from .views import manage_clients, delete_client

urlpatterns = [

    url(r'^manage_clients/(?P<username>[\w.@+-]+)$', manage_clients, name='manage_clients'),
    url(r'^manage_clients/(?P<username>[\w.@+-]+)/(?P<client_id>\d+)$', delete_client, name='delete_client'),
    
]