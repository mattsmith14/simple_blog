from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .models import Post

def index(request):
    posts = Post.objects.filter(published_date__lt=timezone.now())

    context = {
        "posts": posts
    }

    return render(request, "blog/index.html", context)

def post(request, id):
    post = get_object_or_404(Post, pk=id, published_date__lt=timezone.now())

    context = {
        "post": post
    }
    return render(request, "blog/post.html", context)
