from typing import Any
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from consultora import models, forms

# Create your views here.
class Index(TemplateView):
    template_name = 'consultora/index.html'

class ClippingList(ListView):
    model = models.Clipping
    template_name = 'consultora/clipping_list.html'

class ClippingDetail(DetailView):
    model = models.Clipping
    template_name = 'consultora/clipping_detail.html'

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['newspapers'] = models.Newspaper.objects.values_list('name', flat=True).distinct()
        context['form'] = forms.ImageUploadForm()
        context['form_image_article'] = forms.ImageUploadArticle()
        return context

    def post(self, request, pk, *args, **kwargs):
        clipping = models.Clipping.objects.get(pk = pk)

        add_newspaper = request.POST.get('newspaper')
        if add_newspaper:
            newspaper, created = models.Newspaper.objects.get_or_create(name = add_newspaper)
            clipping.newspaper.add(newspaper)
        
        add_article = request.POST.get('add_article')
        if add_article:
            article_newspaper = request.POST.get('article_newspaper')
            article_description = request.POST.get('add_article_description')
            article_url = request.POST.get('add_url')
            article_newspaper = models.Newspaper.objects.get(name = article_newspaper)
            models.Article.objects.create(title=add_article,subtitle=article_description, url = article_url, newspaper=article_newspaper, clipping=clipping)

        delete_article = request.POST.get('delete_article')
        if delete_article:
            newspaper_pk = request.POST.get('newspaper_pk')
            newspaper = models.Newspaper.objects.get(pk = newspaper_pk)
            article = models.Article.objects.get(pk = delete_article, newspaper = newspaper)
            article.delete()


        remove_newspaper = request.POST.get('remove_newspaper')
        if remove_newspaper:
            newspaper = models.Newspaper.objects.get(name=remove_newspaper)
            clipping.newspaper.remove(newspaper)
            print(f'Eliminar {remove_newspaper}')
        
        add_parragraph = request.POST.get('add_parragraph')
        if add_parragraph:
            article_id = request.POST.get('article_id')
            article = models.Article.objects.get(pk=article_id)

            models.Parragraph.objects.create(
                content = add_parragraph,
                article = article
            )

        delete_parragraph = request.POST.get('delete_parragraph_id')
        if delete_parragraph:
            parragraph = models.Parragraph.objects.get(pk = delete_parragraph)
            parragraph.delete()
        
        # form = forms.ImageUploadForm(request.POST, request.FILES)
        # if form.is_valid():
        #     newspaper_pk_img = request.POST.get('newspaper_pk_img')
        #     old_image = models.Newspaper.objects.get(pk = newspaper_pk_img)
        #     image_path = old_image.image.url
        #     print(image_path)

        newspaper_pk_img = request.POST.get('newspaper_pk_img')
        if newspaper_pk_img:
            newspaper = models.Newspaper.objects.get(pk = newspaper_pk_img)
            newspaper.image.delete()
            form = forms.ImageUploadForm(request.POST, request.FILES, instance=newspaper)
            if form.is_valid():
                form.save()

        add_image_article = request.POST.get('add_image_article')
        if add_image_article:
            add_image_article_pk = models.Article.objects.get(pk = add_image_article)
            image = models.Image.objects.create(article = add_image_article_pk)
            form = forms.ImageUploadArticle(request.POST, request.FILES, instance=image)
            if form.is_valid():
                form.save()

        delete_image_article = request.POST.get('delete_image_article')
        if delete_image_article:
            image = models.Image.objects.get(pk = delete_image_article)
            image.image.delete()
            image.delete()


        return HttpResponseRedirect(reverse('consultora:clipping_detail', args=[pk]))
        
        
class NewspaperList(ListView):
    template_name = 'consultora/newspaper.html'
    model = models.Newspaper
