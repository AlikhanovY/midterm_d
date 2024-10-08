from django.shortcuts import render

from .models import Post, Comment


def list_posts(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def post_num(request, pk):
    posts = Post.objects.get(pk = pk)
    print(posts)
    return render(request, 'blog/post_num.html', {'posts': posts})



