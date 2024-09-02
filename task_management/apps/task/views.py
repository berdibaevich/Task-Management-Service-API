import logging

from rest_framework import generics, response, status
from rest_framework import permissions

from .models import Task
from .permissions import IsOwnerOfTask
from .filters import TaskFilter
from .serializers import (
    TaskSerializer, 
    TaskListSerializer, 
    TaskDetailSerializer,
    TaskUpdateSerializer
)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class TaskListApiView(generics.ListAPIView):
    serializer_class = TaskListSerializer
    permission_classes = [permissions.IsAuthenticated]
    filterset_class = TaskFilter


    def get_queryset(self):
        return Task.objects.filter(user = self.request.user)


class TaskDetailOrDeleteApiView(generics.RetrieveDestroyAPIView):
    queryset = Task.objects.all() 
    serializer_class = TaskDetailSerializer
    permission_classes = [IsOwnerOfTask]


class TaskCreateApiView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]


    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data = request.data)
        try:
            serializer.is_valid(raise_exception = True)
            task = serializer.save()
            logging.info(f'Task created successfully by user {request.user.username}. Task ID: {task.id}, Title: {task.title}')
            return response.Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            logging.error(f'Error creating task by user {request.user.username}: {e}')
            return response.Response(
                {'error': 'Task creation failed'},
                status=status.HTTP_400_BAD_REQUEST
            )


class TaskStatusUpdateApiView(generics.UpdateAPIView):
    queryset = Task.objects.all()
    permission_classes = [IsOwnerOfTask]
    serializer_class = TaskUpdateSerializer

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
