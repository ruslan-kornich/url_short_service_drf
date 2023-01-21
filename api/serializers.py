from rest_framework import serializers

from short.models import Url
from short.utils import random_choice
from short.validator import is_valid_url


class ShortURLSerializer(serializers.ModelSerializer):
    class Meta:
        model = Url
        fields = ['pk', 'link', 'short_link', 'time_create', 'end_time']

    def create(self, validated_data):
        link = validated_data['link']
        if is_valid_url(link):
            if Url.objects.filter(link=link).exists():
                link_in_base = Url.objects.get(link=link)
                link_in_base.end_time = validated_data['end_time']
                print(validated_data["end_time"])
                link_in_base.save()
                return link_in_base
            else:
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
