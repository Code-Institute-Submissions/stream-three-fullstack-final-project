from django.conf.urls import url, include
from .views import manage_account

urlpatterns = [

    url(r'^(?P<username>[\w.@+-]+)$', manage_account, name='manage_account'),

]

##(?P<username>[\w.@+-]+)