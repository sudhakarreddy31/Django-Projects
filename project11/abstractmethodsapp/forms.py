from django import forms
from abstractmethodsapp.models import Post


class PostForm(forms.ModelForm):
    model = Post
    fields = ['title', 'content']

