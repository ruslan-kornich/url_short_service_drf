from django.db import models


class Url:
    link = models.URLField(max_length=2083)
    short_link = models.CharField(max_length=255, default='', blank=True)
    time_create = models.DateField(auto_now_add=True)
    end_time = models.DateField()

    def __str__(self):
        return self.short_link
