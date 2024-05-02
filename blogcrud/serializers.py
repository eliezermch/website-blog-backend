from rest_framework import serializers
from django.contrib.auth.models import User
from tasks.serializers import Task_serializer


class User_serializer(serializers.ModelSerializer):
    tasks = Task_serializer(many=True, read_only=True)
    # Ensure password is write-only
    extra_kwargs = {'password': {'write_only': True}}

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'tasks')
