from django.urls import path
from . import controller

urlpatterns = [
    path('', controller.todo_list, name='todo-list'),
    path('<int:id>/', controller.todo_detail, name='todo-detail'),
]
