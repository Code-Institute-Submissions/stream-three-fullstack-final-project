from django.contrib import admin
from .models import Payment, PaymentLineItem
# Register your models here.

admin.site.register(Payment)
admin.site.register(PaymentLineItem)