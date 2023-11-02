from django.urls import path
from portfolio import views

urlpatterns = [
    path('', views.index, name='index'),
    path('soon/', views.soon, name='soon'),
    path('portfolio/', views.PortfolioListView.as_view(), name='portfolio'),
    path('portfolio/<int:pk>', views.PortfolioDetailView.as_view(), name='project'),
    path('skill/', views.SkillListView.as_view(), name='skills'),
    path('skill/<int:pk>', views.SkillDetailView.as_view(), name='skill_detail'),
    path('about/', views.AboutView.as_view(), name = 'about'),
    path('contact/', views.ContactView.as_view(), name = 'contact')
]