from django.contrib import admin
from .models import TaskBoard

class TaskBoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'creator')
    list_filter = ('creator',)
    search_fields = ('name',)

admin.site.register(TaskBoard, TaskBoardAdmin)
