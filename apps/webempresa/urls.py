from django.urls import path
from webempresa import views

app_name = 'WebCompany'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('store/', views.store, name='store'),
    path('contact/', views.contact, name='contact'),
    path('sample/', views.sample, name='sample')
]