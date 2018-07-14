from django.contrib import admin
from .models import UploadModel, Quotes, Invoices, PurchaseOrder
# Register your models here.

admin.site.register(Quotes)
admin.site.register(PurchaseOrder)
admin.site.register(Invoices)
