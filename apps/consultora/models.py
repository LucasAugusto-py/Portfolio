from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Newspaper(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(verbose_name='Newspaper image',upload_to='consultora/newspaper/', blank=True, null=True)
    url = models.URLField(verbose_name='Nespaper url', blank=True, null=True)
    
    created = models.DateField(auto_now_add=True, verbose_name='Created date', null=True, blank=True)
    updated = models.DateField(auto_now=True, verbose_name='Updated Date', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Diario'
        verbose_name_plural = 'Diarios'

class Clipping(models.Model):
    date = models.DateField(auto_created=True)
    newspaper = models.ManyToManyField(Newspaper, blank=True)
    
    created = models.DateField(auto_now_add=True, verbose_name='Created date', null=True, blank=True)
    updated = models.DateField(auto_now=True, verbose_name='Updated Date', null=True, blank=True)

    def __str__(self):
        return f'Clipping {self.date}'
    
    class Meta:
        verbose_name = 'Clipping'
        verbose_name = 'Clippings'
        ordering = ['-created']

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(verbose_name='Subtitle Article')
    url = models.URLField(verbose_name='Url Article', blank=True, null=True)

    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    clipping = models.ForeignKey(Clipping, on_delete=models.CASCADE)

    created = models.DateField(auto_now_add=True, verbose_name='Created date', null=True, blank=True)
    updated = models.DateField(auto_now=True, verbose_name='Updated Date', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Artículo'
        verbose_name_plural = 'Artículo'
        ordering = ['-created']

class Parragraph(models.Model):
    content = RichTextField(verbose_name='Parragraph')

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} parragraph'

    class Meta:
        verbose_name = 'Párrafo'
        verbose_name_plural = 'Párrafos'

class Image(models.Model):
    image = models.ImageField(verbose_name='Image Article', upload_to='consultora/article/', null=True, blank=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} image'

    class Meta:
        verbose_name = 'Imagen'
        verbose_name_plural = 'Imagenes'

