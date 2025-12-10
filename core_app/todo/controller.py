# core_app/todo/controller.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from . import views as todo_service
from .dataclass.todo_dto import TodoData
from .serializer.response.todo_response import TodoResponseSerializer
from .serializer.request.todo_create_request import TodoCreateRequestSerializer
from .serializer.request.todo_update_request import TodoUpdateRequestSerializer

@api_view(['GET', 'POST'])
def todo_list(request):
    if request.method == 'GET':
        todos = todo_service.list_todos()
        serializer = TodoResponseSerializer(todos, many=True)
        return Response(serializer.data)

    # POST
    req_serializer = TodoCreateRequestSerializer(data=request.data)
    if not req_serializer.is_valid():
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    todo_dto: TodoData = req_serializer.to_dataclass()
    todo_id = todo_service.create_todo(todo_dto)
    return Response({'id': todo_id, 'message': 'Created'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    if request.method == 'GET':
        todo = todo_service.get_todo(id)
        if not todo:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoResponseSerializer(todo)
        return Response(serializer.data)

    if request.method == 'PUT':
        existing = todo_service.get_todo(id)
        if not existing:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        req_serializer = TodoUpdateRequestSerializer(data=request.data, partial=True)
        if not req_serializer.is_valid():
            return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        existing_dto = TodoData.from_dict(existing)
        todo_dto = req_serializer.to_dataclass(existing_dto)
        ok = todo_service.update_todo(id, todo_dto)
        if not ok:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return Response({'message': 'Updated'})

    # DELETE
    deleted = todo_service.delete_todo(id)
    if not deleted:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'Deleted'})
