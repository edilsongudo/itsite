from django.shortcuts import render, redirect
from .models import BlogPost


def blog(request):
    posts = BlogPost.objects.all()
    response = render(request, 'blog/blog.html', {'posts': posts})
    return response


def blogpost(request, slug):
    post = BlogPost.objects.get(slug=slug)
    response = render(request, 'blog/blogpost.html', {'post': post})
    return response
