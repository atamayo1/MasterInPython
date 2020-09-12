from rest_framework import serializers
from .models import Page

class PageSerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    title = serializers.CharField()
    content = serializers.CharField()
    slug = serializers.CharField()
    visible = serializers.BooleanField()
    orden = serializers.IntegerField()

    def create(self, validated_data):
        instance = Page()
        instance.title = validated_data.get('title')
        instance.content = validated_data.get('content')
        instance.slug = validated_data.get('slug')
        instance.visible = validated_data.get('visible')
        instance.orden = validated_data.get('orden')
        instance.save()
        return instance