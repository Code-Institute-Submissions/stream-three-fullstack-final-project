from django.conf.urls import url, include
from .views import porthole,delete_file, step_notify  #upload,  #po_upload, invoice_upload
#from .views import delete_quote, delete_po, delete_invoice, step_notify

urlpatterns = [

    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/$', 
                                                    porthole, name='porthole'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/delete_(?P<step>[\w.@+-]+)$', 
                                                    delete_file, name='delete'),
    url(r'^member/(?P<username>[\w.@+-]+)/(?P<client_username>[\w.@+-]+)/(?P<cycle_id>\d+)/notify_(?P<step>[\w.@+-]+)$', 
                                                    step_notify, name='step_notify')                                              
                                          
]

