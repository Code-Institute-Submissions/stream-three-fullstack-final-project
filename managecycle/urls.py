from django.conf.urls import url
from managecycle import views
urlpatterns = [
    
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)$', views.manage_cycles, name='manage_cycles'),
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete$', views.delete_cycle, name='delete_cycle'),
    #url(r'^manage_cycles/(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/edit$', views.edit_cycle, name='edit_cycle'),
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/cancel$', views.cancel_cycle, name='cancel_cycle'),
    url(r'^manage_cycles/(?P<username>[\w.@+-]+)/(?P<cycle_id>\d+)/reset$', views.reset_cycle, name='reset_cycle')
]