from .models import ToDoItem
from .serializers import ToDoItemSerializer
from .permissions import IsOwner
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [IsOwner]

    @action(detail=True)
    def complete(self, request, *args, **kwargs):
        toDoItem = self.get_object()
        toDoItem.complete()
        serializer = ToDoItemSerializer(toDoItem)
        return Response(serializer.data)

    @action(detail=True)
    def uncomplete(self, request, *args, **kwargs):
        toDoItem = self.get_object()
        toDoItem.uncomplete()
        serializer = ToDoItemSerializer(toDoItem)
        return Response(serializer.data)


    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.todo_items.all()