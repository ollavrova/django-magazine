from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions

from posts.models import UserProfile


class CustomAuthentication(authentication.BaseAuthentication):
    def authenticate(self, request):
        email = request.META.get('X_EMAIL')
        if not email:
            return None

        try:
            user = UserProfile.objects.get(email=email)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')

        return (user, None)
