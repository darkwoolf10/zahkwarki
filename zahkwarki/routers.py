from rest_framework import routers
from blog.viewsets import PostViewSet

router = routers.DefaultRouter()
router.register(r'post', PostViewSet)