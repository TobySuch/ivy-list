from rest_framework import serializers
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    completed_at = serializers.ReadOnlyField()
    
    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'created_at', 'completed_at', 'priority']