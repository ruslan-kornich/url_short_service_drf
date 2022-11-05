from rest_framework import serializers

from short.models import Url
from short.utils import random_choice


class ShortURLSerializer(serializers.Serializer):
    link = serializers.CharField(max_length=255)
    end_time = serializers.DateTimeField(required=False)

    def create(self, validated_data):
        short = dict(link=validated_data['link'],
                     short_link=random_choice(),
                     end_time=validated_data['end_time'])
        validated_data.update(short)
        return Url.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.link = validated_data.get('link', instance.link)
        instance.short_link = validated_data.get('short_link', instance.short_link)
        instance.save()
        return instance
