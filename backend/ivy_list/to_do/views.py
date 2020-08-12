from .models import ToDoItem
from .serializers import ToDoItemSerializer
from rest_framework import viewsets


class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)