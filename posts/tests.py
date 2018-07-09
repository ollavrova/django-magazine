from django.test import TestCase
from rest_framework.reverse import reverse
from rest_framework.test import APIRequestFactory
from rest_framework.test import force_authenticate
from django.conf import settings
from posts.api import user_detail
from posts.models import UserProfile


class TestApi(TestCase):
    fixtures = ['initial_data.json']

    def setUp(self):
        self.writer = UserProfile.objects.first()
        self.token = self.writer.auth_token.key
        self.auth_data = {"email": self.writer.email, "password": "adminadmin"}
        self.token_data = {'Authorization': 'Token '+self.token}
        self.editor = UserProfile.objects.create(
            email="google@google.com",
            role=settings.ROLE_CHOICES[1][0],
            date_of_birth="1990-01-02",
            password='123456123'
        )

    def tearDown(self):
        try:
            UserProfile.objects.get(email=self.editor_data['email']).delete()
            UserProfile.objects.get(email=self.writer_data['email']).delete()
            UserProfile.objects.get(email=self.writer['email']).delete()
        except:
            pass

    def test_get_userprofile_by_token(self):
        factory = APIRequestFactory()
        user = UserProfile.objects.get(email=self.writer.email)
        # Make an authenticated request to the view...
        request = factory.get(reverse('user_detail', kwargs={'token': user.auth_token.key}))
        force_authenticate(request, user=user)
        response = user_detail(request, token=user.auth_token.key)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, user.auth_token.key)
        self.assertContains(response, user.email)
        self.assertContains(response, user.date_of_birth)

    def test_endpoints(self):
        """
        test for endpoints
        """
        self.assertEqual(self.client.get(reverse('rest_framework:login')).status_code, 200)
        self.assertEqual(self.client.get(reverse('rest_framework:logout')).status_code, 200)
        self.assertEqual(self.client.get(reverse('approved_list')).status_code, 200)