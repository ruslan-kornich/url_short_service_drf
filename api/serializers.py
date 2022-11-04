from rest_framework import serializers

from short.models import Url


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['short_link', 'link', 'time_create', 'end_time']
