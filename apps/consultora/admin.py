from django.contrib import admin
from consultora import models
# Register your models here.
admin.site.register(models.Newspaper)
admin.site.register(models.Clipping)
admin.site.register(models.Article)
admin.site.register(models.Parragraph)
admin.site.register(models.Image)
