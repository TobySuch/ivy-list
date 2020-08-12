from rest_framework import serializers
from .models import ToDoList, ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    completed_at = serializers.ReadOnlyField()
    todo_list = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'created_at', 'completed_at', 'priority', 'todo_list']

class ToDoListSerializer(serializers.ModelSerializer):
    date = serializers.ReadOnlyField()
    todo_items = ToDoItemSerializer(many=True, read_only=True)

    class Meta:
        model = ToDoList
        fields = ['id', 'date', 'todo_items']
