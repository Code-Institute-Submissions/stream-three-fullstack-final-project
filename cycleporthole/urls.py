from django.conf.urls import url, include
from .views import porthole, upload, delete_file, step_notify #po_upload, invoice_upload
#from .views import delete_quote, delete_po, delete_invoice, step_notify

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/$', 
                                                    porthole, name='porthole'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/upload_(?P<step>[\w.@+-]+)$', 
                                                    upload, name='upload'),
    #url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/po$', 
                                                   # po_upload, name='po_upload'),
    #url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/invoice$', 
                                                   # invoice_upload, name='invoice_upload'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_(?P<step>[\w.@+-]+)$', 
                                                    delete_file, name='delete'),
    #url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_po$', 
                                                    #delete_po, name='delete_po'),
    #url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_invoice$', 
                                                   # delete_invoice, name='delete_invoice'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/notify_(?P<step>[\w.@+-]+)$', 
                                                    step_notify, name='step_notify')                                              
                                          
  
]

