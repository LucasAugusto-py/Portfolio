from django import forms
from consultora import models

class ArticleHead(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title','subtitle', 'url']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'input-custom'
            }),
            'subtitle': forms.Textarea(attrs={
                'class':'input-custom'
            }),
            'url': forms.TextInput(attrs={
                'class':'input-custom'
            })
        }

class Article(forms.ModelForm):
    class Meta:
        model = models.Article
        fields = ['title', 'subtitle']

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = models.Newspaper
        fields = ['image']
        labels = {
            'image':'Imagen'
        }

class ImageUploadArticle(forms.ModelForm):
    class Meta:
        model = models.Image
        fields  = ['image']
        labels = {
            'image': 'Imagen de cabecera'
        }

class ParragraphArticle(forms.ModelForm):
    class Meta:
        model = models.Parragraph
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'class':'input-custom',
            })
        }
        label = {
            'content': 'Parrafo'
        }