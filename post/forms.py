from django import forms
from django.forms import ModelForm

from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {'text': forms.Textarea(attrs={'class': 'form-control'})}
