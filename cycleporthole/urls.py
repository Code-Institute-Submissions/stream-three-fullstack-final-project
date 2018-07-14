from django.conf.urls import url, include
from .views import cycle_porthole

urlpatterns = [

    url(r'^$', 
        cycle_porthole, name='porthole')

  
]
#url(r'^cyle-porthole/(?P<username>[\w.@+-]+)/(?P<id>\d+)/$', 
   # cycle_porthole, name='cycle_porthole')
