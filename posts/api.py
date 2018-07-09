from django.conf import settings
from rest_framework import viewsets, mixins
from rest_framework.authtoken.models import Token
from posts.models import Post, UserProfile
from .serializers import PostSerializer, UserProfileSerializer, UserPostsSerializer, CustomAuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView, ListCreateAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_405_METHOD_NOT_ALLOWED


class UserProfileCreateRetrieveViewSet(mixins.CreateModelMixin,
                                       mixins.RetrieveModelMixin,
                                       viewsets.GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # def get_permissions(self):
    #     if self.action in ['create']:
    #         return (AllowAny(), )

    def retrieve(self, request, token):
        user_token = get_object_or_404(Token, key=token)
        user = get_object_or_404(UserProfile, pk=user_token.user_id)
        serializer = UserProfileSerializer(user)
        return Response({'token': token, 'user': serializer.data})


user_create = UserProfileCreateRetrieveViewSet.as_view({'post': 'create'})
user_detail = UserProfileCreateRetrieveViewSet.as_view({'get': 'retrieve'})


class CustomAuthToken(ObtainAuthToken):
    serializer_class = CustomAuthTokenSerializer


class ApprovedPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'body', 'author__email')
    permission_classes = (AllowAny,)

    def get_queryset(self):
        return Post.objects.filter(approved=True)


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
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


class WritersPostList(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserPostsSerializer

