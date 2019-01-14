from django.shortcuts import render
from django.utils import timezone
from .models import Post, CodexPost
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.all().order_by('created_date')
    users = User.objects.exclude(username='admin')
    return render(request, 'blog/post_list.html', {'posts': posts, 'users': users})


def about(request):
    users = User.objects.exclude(username='admin')
    return render(request, 'blog/about.html', {'users': users})


def show_user_list(request, id):
    try:
        user = User.objects.get(id=id)
        posts = Post.objects.filter(for_whom=id)
        users = User.objects.exclude(username='admin')
    except User.DoesNotExist:
        return render(request, 'not_found.html')
    return render(request, 'blog/show_user_list.html', {'user': user, 'users': users, 'posts': posts})


def codex(request):
    posts = CodexPost.objects.all()
    users = User.objects.exclude(username='admin')
    return render(request, 'blog/codex.html', {'posts': posts, 'users': users})





