from django.contrib import admin
from .models import QuoteStatus, POStatus, InvoicesStatus

# Register your models here.
admin.site.register(QuoteStatus)
admin.site.register(POStatus)
admin.site.register(InvoicesStatus)