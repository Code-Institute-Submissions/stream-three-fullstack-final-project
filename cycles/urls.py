from django.conf.urls import url, include
from .views import member_cycles, client_cycles, reset_search
#from accounts import urls_reset

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/$', member_cycles, name='member_cycles'),
    url(r'^client/(?P<username>[\w.@+-]+)/$', client_cycles, name='client_cycles'),
    url(r'^member/(?P<username>[\w.@+-]+)/$', reset_search, name='reset_search'),
]