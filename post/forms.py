from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    content = forms.TextInput()
    class Meta:
        model = Post
        fields = [
            "title",
            "content",
        ]