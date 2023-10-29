from django.db import models

# Create your models here.
class Newspaper(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(verbose_name='Newspaper image',upload_to='consultora/newspaper/', blank=True, null=True)
    url = models.URLField(verbose_name='Nespaper url', blank=True, null=True)

    def __str__(self):
        return self.name


class Clipping(models.Model):
    date = models.DateField(auto_created=True)
    newspaper = models.ManyToManyField(Newspaper)

    def __str__(self):
        return f'Clipping {self.date}'

class Article(models.Model):
    title = models.CharField(max_length=200)
    subtitle = models.TextField(verbose_name='Subtitle Article')
    url = models.URLField(verbose_name='Url Article', blank=True, null=True)

    newspaper = models.ForeignKey(Newspaper, on_delete=models.CASCADE)
    clipping = models.ForeignKey(Clipping, on_delete=models.CASCADE)
    def __str__(self):
        return self.title

class Parragraph(models.Model):
    content = models.TextField(verbose_name='Parregraph Article')

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} parragraph'

class Image(models.Model):
    image = models.ImageField(verbose_name='Image Article', upload_to='consultora/article/', null=True, blank=True)

    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.article} image'



