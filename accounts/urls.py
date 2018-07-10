from django.conf.urls import url, include
from .views import logout, register
from accounts import urls_reset
#from accounts import urls_reset

urlpatterns = [

    url(r'^logout$', logout, name='logout'),
    url(r'^register$', register, name='register'),
    url(r'^password-reset/', include(urls_reset)),
]