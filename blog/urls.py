from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.post_list, name='post_list'),
    path('about/', views.about, name='about'),
    path('codex/', views.codex, name='codex'),
    path('show_user_list/<int:id>', views.show_user_list, name='user_list'),
]