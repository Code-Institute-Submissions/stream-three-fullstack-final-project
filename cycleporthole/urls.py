from django.conf.urls import url, include
from .views import porthole, quote_upload, po_upload, invoice_upload
from .views import delete_quote, delete_po, delete_invoice

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/$', 
                                                    porthole, name='porthole'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/quote$', 
                                                    quote_upload, name='quote_upload'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/po$', 
                                                    po_upload, name='po_upload'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/invoice$', 
                                                    invoice_upload, name='invoice_upload'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_quote$', 
                                                    delete_quote, name='delete_quote'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_po$', 
                                                    delete_po, name='delete_po'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_invoice$', 
                                                    delete_invoice, name='delete_invoice')                                              
  
]

