from django.conf.urls import url, include
from .views import set_quote_status, set_po_status, set_invoice_status

urlpatterns = [

    url(r'^quote/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                set_quote_status, name='quote_status'),
    url(r'^po/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                set_po_status, name='po_status'),
    url(r'^invoice/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)$', 
                                                                set_invoice_status, name='invoice_status')
  
]
