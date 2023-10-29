from django.shortcuts import render, HttpResponse, get_object_or_404
from webempresa import models

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
    return render(request, 'webempresa/contact.html')

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

def sample(request):
    return HttpResponse('Sample')