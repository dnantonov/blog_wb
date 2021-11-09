from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.auth.models import User


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

