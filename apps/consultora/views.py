from typing import Any
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.urls import reverse, reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
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
        context['form_parragraph'] = forms.ParragraphArticle()
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

        send_email_form = request.POST.get('send_email_form')

        if send_email_form:
            clipping = models.Clipping.objects.get(pk = send_email_form)

            day = clipping.date.day
            month = clipping.date.month
            year = clipping.date.year
            
            html_message = render_to_string('consultora/emails/email_test.html', context={
                'clipping': clipping
            })
            plain_message = strip_tags(html_message)

            message = EmailMultiAlternatives(
                subject = f'Comunicación Estratégica - Clipping de noticias {day}-{month}-{year}',
                body = plain_message,
                from_email = 'settings.EMAIL_HOST_USER',
                to = ['megalucaro@gmail.com']
            )

            message.attach_alternative(html_message, 'text/html')
            message.send()

            # send_mail(
            #     subject= f'Comunicación Estratégica - Clipping de noticias {day}-{month}-{year}',
            #     message= '''
            #     <h1>Hola Este es un titulo</h1>
            #     <p>Este es un parrafo</p>
            #     ''',
            #     from_email= 'settings.EMAIL_HOST_USER',
            #     recipient_list= ['megalucaro@gmail.com'],
            #     fail_silently= False
            # )


        return HttpResponseRedirect(reverse('consultora:clipping_detail', args=[pk]))
        
class ArticleUpdate(UpdateView):
    model = models.Article
    form_class = forms.ArticleHead
    template_name = 'consultora/updates/article_update_form.html'

    def get_success_url(self):
        return reverse_lazy('consultora:clipping_detail', args=[self.object.clipping.id]) + f'#newspaper-{self.object.newspaper.id}'

class ArticleDelete(DeleteView):
    model = models.Article
    template_name = 'consultora/deletes/article_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('consultora:clipping_detail', args=[self.object.clipping.id]) + f'#newspaper-{self.object.newspaper.id}'

class ParragraphUpdate(UpdateView):
    model = models.Parragraph
    form_class = forms.ParragraphArticle
    template_name = 'consultora/updates/parragraph_update_form.html'

    def get_success_url(self):
        return reverse_lazy('consultora:clipping_detail', args=[self.object.article.clipping.id]) + f'#article-content-{self.object.article.id}'
    
class ParragraphDelete(DeleteView):
    model = models.Parragraph
    template_name = 'consultora/deletes/parragraph_confirm_delete.html'

    def get_success_url(self):
        return reverse_lazy('consultora:clipping_detail', args = [ self.object.article.clipping.id ]) + f'#article-content-{self.object.article.id}'
        
class NewspaperList(ListView):
    template_name = 'consultora/newspaper.html'
    model = models.Newspaper
