from django.urls import path, include
from . import views

urlpatterns = [
    path('api/list/', views.TaskListCreateAPIView.as_view()),
    path('api/taskboard/<int:taskboard_id>/', views.GetTasksByTaskBoardAPIView.as_view()),
]