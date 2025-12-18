from django.urls import path
from .controller import TodoController

urlpatterns = [
    path("create/", TodoController.create),
    path("", TodoController.get_all),
    path("get/", TodoController.get_one),
    path("update/", TodoController.update),
    path("delete/", TodoController.delete),
]
