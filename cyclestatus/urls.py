from django.conf.urls import url, include
from .views import set_quote_status 

urlpatterns = [

    url(r'^quote/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                set_quote_status, name='quote_status'),
  
]
