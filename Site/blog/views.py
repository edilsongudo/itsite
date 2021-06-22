from django.shortcuts import render, redirect
from .models import BlogPost


def blog(request):
    posts = BlogPost.objects.all()
    response = render(request, 'blog/blog.html', {'posts': posts})
    return response
