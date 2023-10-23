from django.db import models

# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=200, verbose_name='Skill')
    image = models.ImageField(verbose_name='Skill Image', blank=True, null=True)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'skill'
        verbose_name_plural = 'skills'

class Project(models.Model):
    name = models.CharField(max_length=200, verbose_name='Project Name')
    description = models.TextField(verbose_name='Project Description')
    url = models.CharField(max_length=200, verbose_name='Project url', null=True, blank=True)
    github_link = models.URLField(max_length=300, verbose_name='Link to Github', null=True, blank=True)
    image = models.ImageField(verbose_name='Image file', null=True, blank=True)
    image_url = models.URLField(max_length=300, verbose_name='Image url', null=True, blank=True)

    def __str__(self):
        return f'{self.name}'

    #Many to Many relationship
    skills = models.ManyToManyField(Skill, blank=True)

    class Meta:
        verbose_name = 'project'
        verbose_name_plural = 'projects'