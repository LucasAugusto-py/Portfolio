from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    #Portfolio/Principal Path
    path('', include('portfolio.urls')),
    #Project paths
    path('company-website/', include('webempresa.urls')),
    #Admin path
    path('admin/', admin.site.urls),
]

if settings.DEBUG: 
    from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
    #urlpatterns += staticfiles_urlpatterns
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

