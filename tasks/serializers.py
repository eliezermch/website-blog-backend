from rest_framework import serializers
from .models import Task


class Task_serializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'title', 'description', 'done', 'created_at')
        read_only_fields = ('id', 'created_at')

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        return super().create(validated_data)
