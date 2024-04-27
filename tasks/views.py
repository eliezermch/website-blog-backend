from rest_framework import viewsets, permissions
from .models import Task
from .serializers import Task_serializer
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = Task_serializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)

    @action(detail=True, methods=['post'])
    def done(self, request, pk=None):
        task = self.get_object()
        task.done = not task.done
        task.save()
        return Response({
            'status': 'task done' if task.done else 'task undone'
        }, status=status.HTTP_200_OK)
