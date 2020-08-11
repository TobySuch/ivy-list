from django.db import models
from django.conf import settings

class ToDoItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, help_text="Add more details here. You can use markdown to format it!")
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=True, null=False)