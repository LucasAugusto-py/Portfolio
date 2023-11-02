from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.urls import reverse
from webempresa import models, forms

# Create your views here.
def home(request):
    return render(request, 'webempresa/home.html')

def about(request):
    return render(request, 'webempresa/about.html')

def services(request):
    services = models.Service.objects.all()

    return render(request, 'webempresa/services.html', context={
        'services': services
    })

def store(request):
    return render(request, 'webempresa/store.html')

def contact(request):
    form_contact = forms.ContactForm()

    if request.method == 'POST':
        contact_form = forms.ContactForm(data = request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            content = request.POST.get('content', '')

            return redirect(reverse('WebCompany:contact')+'?ok')

    return render(request, 'webempresa/contact.html', {
        'form_contact':form_contact
    })

def blog(request):
    posts = models.Post.objects.all()

    return render(request, 'webempresa/blog.html', context={
        'posts': posts
    })

def category(request, pk):
    category = get_object_or_404(models.Category, id = pk)

    return render(request, 'webempresa/category.html', context={
        'category': category
    })

def sample(request, pk, page_slug):
    page = get_object_or_404(models.Page, id = pk)
    return render(request, 'webempresa/sample.html', {'page':page})