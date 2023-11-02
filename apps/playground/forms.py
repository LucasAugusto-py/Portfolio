from django import forms
from playground import models

class PageForm(forms.ModelForm):
    
    class Meta:
        model = models.Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={
                'class':'form-control'
            }),
            'content': forms.Textarea(attrs={
                'class':'form-control'
            }),
            'order': forms.NumberInput(attrs={
                'class':'form-control'
            })
        }
        labels = {
            'title': 'Título',
            'content': 'Contenido',
            'order': 'Orden'
        }