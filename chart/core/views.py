from django.shortcuts import render
from .models import Post
def home(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'index.html', context)

def bar(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'bar.html', context)

def line(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'line.html', context)

def pie(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'pie.html', context)

def flow(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'flow.html', context)

def gantt(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'gantt.html', context)

def solid(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'solid.html', context)


