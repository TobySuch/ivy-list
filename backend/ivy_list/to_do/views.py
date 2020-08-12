from .models import ToDoList, ToDoItem
from .serializers import ToDoListSerializer, ToDoItemSerializer
from .permissions import IsOwner
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

class ToDoListViewSet(viewsets.ModelViewSet):
    queryset = ToDoList.objects.all()
    serializer_class = ToDoListSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get_queryset(self):
        return self.request.user.todo_lists.all()

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated]

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

    def get_queryset(self):
        return ToDoItem.objects.filter(todo_list__user=self.request.user)


    

    