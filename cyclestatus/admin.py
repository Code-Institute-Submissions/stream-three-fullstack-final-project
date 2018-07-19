from django.contrib import admin
from cyclestatus import models

# Register your models here.
admin.site.register(models.QuoteStatus)
admin.site.register(models.POStatus)
admin.site.register(models.InvoicesStatus)
admin.site.register(models.QuoteUrgency)
admin.site.register(models.POUrgency)
admin.site.register(models.InvoiceUrgency)
admin.site.register(models.QuoteAction)
admin.site.register(models.POAction)
admin.site.register(models.InvoiceAction)