from django.contrib import admin
from cyclestatus import models

# Register your models here.
admin.site.register(models.QuoteStatus)
admin.site.register(models.POStatus)
admin.site.register(models.InvoicesStatus)
