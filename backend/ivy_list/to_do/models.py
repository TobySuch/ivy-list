from django.db import models
from django.conf import settings
import datetime
from django.contrib.auth import get_user_model

class ToDoItem(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, related_name="todo_items", on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=120, blank=False)
    description = models.TextField(blank=True, help_text="Add more details here. You can use markdown to format it!")
    created_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)
    priority = models.IntegerField(blank=False, null=False, default=1)

    def complete(self):
        self.completed_at = datetime.datetime.now()
        self.save()

    def uncomplete(self):
        self.completed_at = None
        self.save()

    def __str__(self):
        return self.title