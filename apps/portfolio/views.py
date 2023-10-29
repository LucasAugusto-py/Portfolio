from typing import Any
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from portfolio import models, forms

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

class SkillListView(ListView):
    model = models.Skill
    template_name = 'portfolio/skill_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['image_form_skill'] = forms.SkillImageForm()

        return context
    
    def post(self, request, *args, **kwargs):
        skill = models.Skill.objects.get(pk = request.POST.get('skill_id'))

        form_image = forms.SkillImageForm(request.POST, request.FILES, instance=skill)
        if form_image.is_valid():
            form_image.save()
        
        return HttpResponseRedirect(reverse('skills'))

class SkillDetailView(DetailView):
    model = models.Skill
    template_name = 'portfolio/skill_detail.html'