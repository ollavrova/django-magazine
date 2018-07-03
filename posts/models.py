from django.db import models
from django.contrib.auth.models import User


class Posts(models.Model):
    title = models.TextField()
    body = models.TextField()
    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)
