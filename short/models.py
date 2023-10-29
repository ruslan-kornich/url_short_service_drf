from django.db import models
from accounts.models import CustomUser


class Url(models.Model):
    objects = models.Manager()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    link = models.CharField(max_length=2083)
    short_link = models.CharField(max_length=255, default="", blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)
    clicks = models.IntegerField(default=0)

    def __str__(self):
        return self.short_link
