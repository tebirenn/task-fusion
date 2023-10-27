from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import TaskBoard
from .serializers import TaskBoardSerializer


class TaskBoardListCreateAPIView(generics.ListCreateAPIView):
    queryset = TaskBoard.objects.all()
    serializer_class = TaskBoardSerializer  
    authentication_classes = (JWTAuthentication,)

    def perform_create(self, serializer):
        current_user = self.request.user
        serializer.save(creator=current_user)


class GetTaskBoardListByUserAPIView(APIView):
    def get(self, request):
        task_boards = TaskBoard.objects.filter(creator=self.request.user)
        serializer = TaskBoardSerializer(task_boards, many=True)
        return Response(serializer.data)