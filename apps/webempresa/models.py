from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name='Title')
    subtitle = models.CharField(max_length=200, verbose_name='Subtitle')
    content = models.TextField(verbose_name='Content description', )
    image = models.ImageField(verbose_name='Image', upload_to = 'services')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    class Meta:
        verbose_name = 'service'
        verbose_name_plural = 'services'
        ordering = ['-created']

    def __str__(self):
        return self.title
    
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='Category name')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    class Meta:
        verbose_name = 'category'
        verbose_name_plural = 'categories'
        ordering = ['-created']

    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title post')
    content = models.TextField(verbose_name='Content')
    published = models.DateTimeField(verbose_name='Publish date', default = now)
    image = models.ImageField(verbose_name='Image post', upload_to='blog', null=True, blank=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, verbose_name='Categories', related_name='get_posts')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Created date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Updated Date')

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ['-created']

    def __str__(self):
        return self.title