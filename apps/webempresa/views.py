from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'webempresa/home.html')

def about(request):
    return render(request, 'webempresa/about.html')

def services(request):
    return render(request, 'webempresa/services.html')

def store(request):
    return render(request, 'webempresa/store.html')

def contact(request):
    return render(request, 'webempresa/contact.html')

def sample(request):
    return HttpResponse('Sample')