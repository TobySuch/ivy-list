from .models import ToDoItem
from .serializers import ToDoItemSerializer
from .permissions import IsOwner
from .pagination import StandardResultsSetPagination
from rest_framework import permissions, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
import datetime
    

class ToDoItemViewSet(viewsets.ModelViewSet):
    queryset = ToDoItem.objects.all()
    serializer_class = ToDoItemSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]
    pagination_class = StandardResultsSetPagination

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
        if "priority" not in serializer.validated_data.keys():
            number_of_tasks_today = ToDoItem.objects.filter(
                owner=self.request.user, date=serializer.validated_data["date"]).count()
            priority=number_of_tasks_today + 1
        else:
            priority = serializer.validated_data["priority"]

        serializer.save(owner=self.request.user,
            priority=priority)

    def get_queryset(self):
        queryset =  self.request.user.todo_items.all()
        date = self.request.query_params.get('date', None)
        if date is not None:
            queryset = queryset.filter(date=date)

        queryset = queryset.order_by('-date')
        return queryset
