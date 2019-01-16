from django.shortcuts import render
from .models import Post, CodexPost
from rest_framework import viewsets
from blog.serializers import UserSerializer, GroupSerializer, CodexSerializer, PostSerializer
from django.contrib.auth.models import User, Group


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


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class CodexViewSet(viewsets.ModelViewSet):
    queryset = CodexPost.objects.all()
    serializer_class = CodexSerializer