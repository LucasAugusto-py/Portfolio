from django.contrib import admin
from webempresa import models
# Register your models here.
class ServiceAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(models.Service ,ServiceAdmin)