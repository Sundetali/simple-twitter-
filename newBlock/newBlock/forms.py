from django import forms

from .models import Post, Comment

class MyModel(forms.ModelForm):
    class Meta:
        model = newModel
        fields = ('title', 'text', 'thumb')

