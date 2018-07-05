from rest_framework import serializers
from .models import Post, UserProfile


class CustomUserDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'
        read_only_fields = ('email',)


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserProfile
        fields = '__all__'


class UserPostsSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True)

    class Meta:
        model = UserProfile
        fields = ('email', 'role', 'posts')

