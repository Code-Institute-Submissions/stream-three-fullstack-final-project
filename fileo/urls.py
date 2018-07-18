"""fileo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from accounts.views import index
from accounts import urls as urls_accounts
from cycles import urls as urls_cycles
from manageclient import urls as urls_manage_client
from profiles import urls as urls_profiles
from cycleporthole import urls as urls_porthole
from cyclestatus import urls as urls_status
from fileo.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^media/(?P<path>.*)$', static.serve, {'document_root': MEDIA_ROOT}),
    url(r'^$', index, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^cycles/', include(urls_cycles)),
    url(r'^profile/', include(urls_manage_client)),
    url(r'^profile/', include(urls_profiles)),
    url(r'^porthole/', include(urls_porthole)),
    url(r'^status/', include(urls_status)),
   
]
