from django.conf.urls import url, include
from .views import logout, member_cycles, client_cycles
#from accounts import urls_reset

urlpatterns = [

    url(r'^logout$', logout, name='logout'),
    url(r'^member/(?P<username>[\w.@+-]+)/$', member_cycles, name='member_cycles'),
    url(r'^client/(?P<username>[\w.@+-]+)/$', client_cycles, name='client_cycles'),
]