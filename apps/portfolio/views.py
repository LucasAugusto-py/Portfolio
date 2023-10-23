from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from portfolio import models

def index(request):
    return render(request, 'core/index.html')

def soon(request):
    return render(request, 'core/soon.html')

class PortfolioListView(ListView):
    model = models.Project
    template_name = 'portfolio/portfolio.html'

class PortfolioDetailView(DetailView):
    model = models.Project
    template_name = 'portfolio/project_detail.html'