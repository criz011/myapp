from drf_spectacular.utils import extend_schema
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .dataclass.request.create import CreateTodoData
from .dataclass.request.update import UpdateTodoData

from .serializer.request.create import TodoCreateRequestSerializer
from .serializer.request.update import TodoUpdateRequestSerializer

from .views import TodoView


class TodoController:

    @extend_schema(
        description="Create a Todo item",
        request=TodoCreateRequestSerializer,
    )
    @api_view(['POST'])
    def create_item(request: Request) -> Response:
        todo_data = CreateTodoData(**request.data)
        return TodoView().create_todo(params=todo_data.__dict__)

    @extend_schema(
        description="Get a single Todo or all Todos",
    )
    @api_view(['GET'])
    def get_item(request: Request, todo_id: int = None) -> Response:
        return TodoView().get_todo(todo_id=todo_id)

    @extend_schema(
        description="Update a Todo item",
        request=TodoUpdateRequestSerializer,
    )
    @api_view(['PUT'])
    def update_item(request: Request, todo_id: int) -> Response:
        todo_data = UpdateTodoData(**request.data)
        return TodoView().update_todo(todo_id=todo_id, params=todo_data.__dict__)

    @extend_schema(
        description="Delete a Todo item",
    )
    @api_view(['DELETE'])
    def delete_item(request: Request, todo_id: int) -> Response:
        return TodoView().delete_todo(todo_id=todo_id)
