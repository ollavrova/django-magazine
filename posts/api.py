from django.conf import settings
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, UserProfile
from .serializers import PostSerializer, UserProfileSerializer, UserPostsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import  AllowAny
from rest_framework.response import Response
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED


class ApprovedPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'body', 'author__email')
    authentication_classes = (AllowAny,)

    def get_queryset(self):
        return Post.objects.filter(approved=True)


class UserProfileDetail(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication, )


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'body', 'author__email')
    pagination_class = LimitOffsetPagination

    def post(self, request, *args, **kwargs):
        try:
            author = UserProfile.objects.get(id=int(request.data['author']))
        except Exception as e:
            return Response({str(e)}, status=HTTP_400_BAD_REQUEST)
        if author.role == settings.ROLE_CHOICES[0][0]:  # if author is a writer then allowed to make post
            return self.create(request, *args, **kwargs)
        else:
            return Response({"detail": "Only writers allowed to create a POST."}, status=HTTP_405_METHOD_NOT_ALLOWED)


class WritersPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = UserPostsSerializer
    authentication_classes = (TokenAuthentication,)
