from django.conf.urls import url, include
from .views import porthole, quote_upload

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/$', 
                                                    porthole, name='porthole'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/quote$', 
                                                    quote_upload, name='quote_upload'),
  
]
#url(r'^cyle-porthole/(?P<username>[\w.@+-]+)/(?P<id>\d+)/$', 
   # cycle_porthole, name='cycle_porthole')
