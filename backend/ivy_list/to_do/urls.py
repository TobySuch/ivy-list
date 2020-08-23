from . import views
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'todo_list', views.ToDoListViewSet)
router.register(r'todo_item', views.ToDoItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]