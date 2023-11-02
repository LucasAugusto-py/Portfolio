from typing import Any
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse, reverse_lazy
from playground import models
from django.shortcuts import render
from playground import forms

# Create your views here.
class HomePageView(TemplateView):
    template_name = 'playground/home.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['title']  = 'Mi super web playground'

        return context
    
    def get(self, request, *args, **kwargs):
       return render(request, self.template_name, {'title':'rompiendo todo'})
    
class PageListView(ListView):
    model = models.Page

class PageDetailView(DetailView):
    model = models.Page

class SamplePageView(TemplateView):
    template_name = 'playground/sample.html'

class PageCreate(CreateView):
    model = models.Page
    form_class = forms.PageForm
    success_url = reverse_lazy('playground:pages')

    # def get_success_url(self):
    #     return reverse('playground:pages')

class PageUpdate(UpdateView):
    model = models.Page
    form_class = forms.PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('playground:update', args=[self.object.id]) + '?ok'
    
class PageDelete(DeleteView):
    model = models.Page
    success_url = reverse_lazy('playground:pages')
