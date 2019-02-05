from rest_framework import serializers
from .models import Post, CodexPost
from django.contrib.auth.models import User, Group


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')


class CodexSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CodexPost
        fields = '__all__'


class PostSerializer(serializers.HyperlinkedModelSerializer):
    author = UserSerializer()
    # id = serializers.Field()

    class Meta:
        model = Post
        fields = ('id', 'author', 'for_whom', 'text', 'punishment_count', 'punishment_type', 'punishment_quantity')
