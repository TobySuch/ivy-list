from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import ToDoList, ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    completed_at = serializers.ReadOnlyField()
    todo_list = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'created_at', 'completed_at', 'priority', 'todo_list']

class ToDoListSerializer(serializers.ModelSerializer):
    todo_items = ToDoItemSerializer(many=True, read_only=True)

    def validate_date(self, value):
        if self.instance and self.instance.date != value:
            raise ValidationError("You may not edit date!")
        return value

    class Meta:
        model = ToDoList
        fields = ['id', 'date', 'todo_items']
