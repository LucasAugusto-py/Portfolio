from django.urls import path
from playground import views

app_name = 'playground'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('pages/', views.PageListView.as_view(), name = 'pages'),
    path('pages/<int:pk>/<slug:slug>/', views.PageDetailView.as_view(), name = 'page'),
    path('sample/', views.SamplePageView.as_view(), name = 'sample'),
    path('create/', views.PageCreate.as_view(), name = 'create'),
    path('update/<int:pk>/', views.PageUpdate.as_view(), name = 'update'),
    path('delete/<int:pk>', views.PageDelete.as_view(), name = 'delete'),
]