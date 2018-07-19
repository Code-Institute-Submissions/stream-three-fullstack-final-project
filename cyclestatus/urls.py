from django.conf.urls import url, include
from cyclestatus import views


urlpatterns = [

    url(r'^quote/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                views.set_quote_status, name='quote_status'),
    url(r'^po/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                views.set_po_status, name='po_status'),
    url(r'^invoice/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                views.set_invoice_status, name='invoice_status'),
    url(r'^quote/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/urgent$', 
                                                                views.set_quote_urgency, name='quote_urgency'),
    url(r'^po/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/urgent$', 
                                                                views.set_po_urgency, name='po_urgency'),
    url(r'^invoice/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/urgent$', 
                                                                views.set_invoice_urgency, name='invoice_urgency')
  
]
