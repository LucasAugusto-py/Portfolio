from django.contrib import admin
from playground import models

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('title','order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(models.Page, PageAdmin)