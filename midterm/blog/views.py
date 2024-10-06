from django.shortcuts import render

from .models import Post, Comment


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list')

