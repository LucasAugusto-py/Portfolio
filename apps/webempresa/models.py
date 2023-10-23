from django.db import models

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