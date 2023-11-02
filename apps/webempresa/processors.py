from webempresa import models

def ctx_dict(request):
    ctx = {}
    links = models.Link.objects.all()
    for link in links:
        ctx[link.key] =  link.url

    return ctx