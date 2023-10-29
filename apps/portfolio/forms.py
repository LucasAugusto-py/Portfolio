from django import forms
from portfolio import models


class SkillImageForm(forms.ModelForm):
    class Meta:
        model = models.Skill
        fields = ['image']
