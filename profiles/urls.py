from django.conf.urls import url
from .views import member_profile, client_profile
#from accounts import urls_reset

urlpatterns = [

    url(r'^edit/(?P<username>[\w.@+-]+)/$', member_profile, name='member_profile'),
    url(r'^edit/(?P<username>[\w.@+-]+)/(?P<client_id>\d+)$', client_profile, name='client_profile')
   
]