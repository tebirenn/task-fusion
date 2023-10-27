from django.urls import path, include
from . import views

urlpatterns = [
    path('api/list/', views.TaskBoardListCreateAPIView.as_view(), name='taskboard-list-create'),
    path('api/user/taskboards/', views.GetTaskBoardListByUserAPIView.as_view()),
]