from django.conf.urls import url, include
from .views import member_cycles, client_cycles, reset_search


urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/$', member_cycles, name='member_cycles'),
    url(r'^client/(?P<username>[\w.@+-]+)/$', client_cycles, name='client_cycles'),
    url(r'^(?P<username>[\w.@+-]+)/reset-search$', reset_search, name='reset_search'),
]