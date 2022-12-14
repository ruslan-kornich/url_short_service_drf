from django.db import models


class Url(models.Model):
    objects = models.Manager()
    link = models.CharField(max_length=2083)
    short_link = models.CharField(max_length=255, default='', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True)

    def __str__(self):
        return self.short_link

