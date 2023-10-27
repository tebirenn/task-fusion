from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication

from .models import Task
from .serializers import TaskSerializer

class TaskListCreateAPIView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (JWTAuthentication, )

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(creator=current_user)


class GetTasksByTaskBoardAPIView(APIView):
    def get(self, request, taskboard_id):
        tasks = Task.objects.filter(task_board_id=taskboard_id)
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)