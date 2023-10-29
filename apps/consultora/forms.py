from django import forms
from consultora import models

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = models.Newspaper
        fields = ['image']

class ImageUploadArticle(forms.ModelForm):
    class Meta:
        model = models.Image
        fields  = ['image']
