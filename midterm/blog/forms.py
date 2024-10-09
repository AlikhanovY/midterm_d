from django import forms
from .models import Post  # Import the Post model that the form will be based on

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']  # List of fields from the Post model that you want to include in the form
