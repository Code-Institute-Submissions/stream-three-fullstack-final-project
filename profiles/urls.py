from django.conf.urls import url
from .views import member_profile
#from accounts import urls_reset

urlpatterns = [

    url(r'^edit/(?P<username>[\w.@+-]+)/$', member_profile, name='member_profile'),
   
]