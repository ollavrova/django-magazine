from rest_framework.authtoken.models import Token
from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination

from posts.models import Post, UserProfile
from .serializers import PostSerializer, UserProfileSerializer, PostsWriterSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED, HTTP_202_ACCEPTED


class ApprovedPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'body', 'author__email')

    def get_queryset(self):
        return Post.objects.filter(approved=True)


class UserProfileDetail(RetrieveAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    authentication_classes = (TokenAuthentication, )


class PostList(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)
    filter_backends = (SearchFilter,)
    search_fields = ('title', 'body', 'author__email')
    pagination_class = LimitOffsetPagination


class WritersPostList(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostsWriterSerializer
    # permission_classes = (IsAuthenticated,)
    authentication_classes = (TokenAuthentication,)


class Login(APIView):

    def post(self, request, format=None):
        try:
            userprofile = UserProfile.objects.get(email=request.get('email'))
            Token.objects.get(user=userprofile)
            statusCode = HTTP_202_ACCEPTED
        except UserProfile.DoesNotExist:
            user = UserProfile.objects.create(email=request.get('email'),
                                              date_of_birth=request.get('date_of_birth'),
                                              role=request.get('role'))
            statusCode = HTTP_201_CREATED
            return Response({'user is created'}, statusCode)
        except Exception as e:
            return Response({'user is not created - '+str(e.message)}, status=HTTP_400_BAD_REQUEST)


