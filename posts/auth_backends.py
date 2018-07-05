from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model


class CustomUserModelBackend(ModelBackend):
    def authenticate(self, email=None, password=None):
        try:
            user = get_user_model().objects.get(email=email)
            if user.check_password(password):
                return user
        except:
            return None

    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except:
            return None
