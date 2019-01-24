from rest_framework import routers
from blog.viewsets import PostsViewSet, UsersViewSet

router = routers.DefaultRouter()
router.register(r'posts', PostsViewSet)
router.register(r'users', UsersViewSet)
