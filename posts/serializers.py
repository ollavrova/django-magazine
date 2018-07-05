from rest_framework import serializers
from .models import Post, UserProfile


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('email', 'role', 'date_of_birth', 'is_active', 'is_staff', 'is_admin')
        read_only_fields = ('email',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'created', 'author', 'approved')


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = ('email', 'role', 'date_of_birth', 'is_active', 'is_staff', 'is_admin')


class PostsWriterSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = UserProfile
        fields = ('id', 'email', 'posts')

