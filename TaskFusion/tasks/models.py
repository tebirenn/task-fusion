from django.db import models
from django.contrib.auth.models import User

from taskboards.models import TaskBoard

PRIORITY_CHOICES = (
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
)

STATUS_CHOICES = (
    ('todo', 'To Do'),
    ('in_progress', 'In Progress'),
    ('done', 'Done'),
)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    due_date = models.DateTimeField()
    priority = models.CharField(max_length=20, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    task_board = models.ForeignKey(TaskBoard, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
