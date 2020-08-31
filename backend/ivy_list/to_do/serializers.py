from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import ToDoItem

class ToDoItemSerializer(serializers.ModelSerializer):
    completed_at = serializers.ReadOnlyField()

    def validate_date(self, value):
        if self.instance and self.instance.date != value:
            raise ValidationError("You may not edit date!")
        return value

    class Meta:
        model = ToDoItem
        fields = ['id', 'title', 'description', 'date', 'created_at', 'completed_at', 'priority']
