from django.conf.urls import url, include
from .views import porthole

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)/cycle/(?P<id>\d+)$', porthole, name='porthole')
  
]
#url(r'^cyle-porthole/(?P<username>[\w.@+-]+)/(?P<id>\d+)/$', 
   # cycle_porthole, name='cycle_porthole')
