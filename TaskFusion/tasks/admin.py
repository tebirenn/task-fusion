from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'due_date', 'priority', 'status', 'creator', 'task_board')
    list_filter = ('priority', 'status', 'creator', 'task_board')
    search_fields = ('title', 'description')
    date_hierarchy = 'due_date'

admin.site.register(Task, TaskAdmin)
