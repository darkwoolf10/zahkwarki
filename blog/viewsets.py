from rest_framework import viewsets
from .models import Post
from .serializers import ArticleSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = ArticleSerializer