from django.conf.urls import url, include
from .views import logout, member_cycles
#from accounts import urls_reset

urlpatterns = [

    url(r'^logout$', logout, name='logout'),
    url(r'^member/$', member_cycles, name="member_cycles"),
]