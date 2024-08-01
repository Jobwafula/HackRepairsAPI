from rest_framework import serializers
from dev.models import Screen, ScreenElement, ScreenAction, UserInteraction, order


class ScreenSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    description = serializers.TextField(blank=True, null=True)
    url = serializers.URLField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()

    def create(self, data):
        return Screen.objects.create(**data)
