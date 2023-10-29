from django.urls import path
from consultora import views
from django.conf import settings

app_name = 'consultora'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('clipping/', views.ClippingList.as_view(), name='clipping_list'),
    path('clipping/<int:pk>', views.ClippingDetail.as_view(), name='clipping_detail'),
    path('newspaper/', views.NewspaperList.as_view(), name='newspaper')
]

