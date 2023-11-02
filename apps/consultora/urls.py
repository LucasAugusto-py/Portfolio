from django.urls import path
from consultora import views
from django.conf import settings

app_name = 'consultora'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('clipping/', views.ClippingList.as_view(), name='clipping_list'),
    path('clipping/<int:pk>/', views.ClippingDetail.as_view(), name='clipping_detail'),
    path('newspaper/', views.NewspaperList.as_view(), name='newspaper'),
    path('article/<int:pk>/', views.ArticleUpdate.as_view(), name='article_update'),
    path('article/delete/<int:pk>/', views.ArticleDelete.as_view(), name = 'delete_article'),
    path('parragraph/<int:pk>/', views.ParragraphUpdate.as_view(), name='parragraph_update'),
    path('article/delete/parragraph/<int:pk>/', views.ParragraphDelete.as_view(), name = 'parragraph_delete')
]

