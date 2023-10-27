from rest_framework import serializers
from .models import TaskBoard


class TaskBoardSerializer(serializers.ModelSerializer):
    creator = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = TaskBoard
        fields = '__all__'
