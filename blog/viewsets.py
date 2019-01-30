from django.contrib.auth.models import User, Group
from .models import Post, CodexPost
from rest_framework import viewsets
from .serializers import PostSerializer, UserSerializer, GroupSerializer, CodexSerializer


class PostsViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class UsersViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.exclude(username='admin').order_by('-date_joined')
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
