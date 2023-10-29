from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class CustomUser(AbstractUser):
    full_name = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    date_joined = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.username
