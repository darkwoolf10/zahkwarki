from django.shortcuts import render
from .models import Post, CodexPost
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)


@csrf_exempt
@api_view(["GET"])
def sample_api(request):
    data = {'sample_data': 123}
    return Response(data, status=HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def punishment_up(request, id):
    post = Post.objects.get(id=id)
    if post:
        post.punishment_count += post.punishment_quantity
        post.save()
        return Response({'success': True}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Post not found'}, status=HTTP_404_NOT_FOUND)


@csrf_exempt
@api_view(["POST"])
def punishment_down(request, id):
    post = Post.objects.get(id=id)
    if post:
        post.punishment_count -= post.punishment_quantity
        post.save()
        return Response({'success': True}, status=HTTP_200_OK)
    else:
        return Response({'error': 'Post not found'}, status=HTTP_404_NOT_FOUND)


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
