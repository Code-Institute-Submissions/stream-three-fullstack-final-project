from django.conf.urls import url
from .views import manage_cycles, delete_cycle

urlpatterns = [
    
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)$', manage_cycles, name='manage_cycles'),
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete$', delete_cycle, name='delete_cycle'),

]