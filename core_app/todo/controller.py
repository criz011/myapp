from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from typing import Any, Iterable

from . import views as todo_service
from .dataclass.todo_dto import TodoData

from .serializer.request.create import TodoCreateRequestSerializer
from .serializer.request.update import TodoUpdateRequestSerializer
from .serializer.request.get_all import TodoListRequestSerializer

from .serializer.response.get import TodoGetResponseSerializer
from .serializer.response.get_all import TodoListResponseSerializer
from .serializer.response.create import TodoCreateResponseSerializer
from .serializer.response.update import TodoUpdateResponseSerializer


def _serialize_and_respond(obj: Any, serializer_cls, many: bool = False, http_status=status.HTTP_200_OK):

    # list of dicts
    if many:
        if isinstance(obj, Iterable) and all(isinstance(i, dict) for i in obj):
            # wrapper serializer like TodoListResponseSerializer expects {"results": [...], "count": N}
            if serializer_cls is TodoListResponseSerializer:
                return Response({"results": obj, "count": len(obj)}, status=http_status)
            return Response(obj, status=http_status)

        # else use serializer for many=True
        ser = serializer_cls(obj, many=True)
        return Response(ser.data, status=http_status)

    # single object
    if isinstance(obj, dict):
        return Response(obj, status=http_status)

    ser = serializer_cls(obj)
    return Response(ser.data, status=http_status)


@api_view(['GET', 'POST'])
def todo_list(request):
    # GET /todo/
    if request.method == 'GET':
        # optionally validate query params
        qs_ser = TodoListRequestSerializer(data=request.query_params)
        if not qs_ser.is_valid():
            # If you want to ignore invalid query params, you can skip this check
            return Response(qs_ser.errors, status=status.HTTP_400_BAD_REQUEST)

        qd = qs_ser.validated_data
        # pass filters/pagination to service if you implemented that layer
        todos = todo_service.list_todos()  # could be list[model] or list[dict]

        # Use list-response wrapper if you prefer, else plain list
        # If you want wrapper: use TodoListResponseSerializer, else use TodoGetResponseSerializer(many=True)
        # Here we try the wrapper first (company-style)
        if isinstance(todos, list):
            return _serialize_and_respond(todos, TodoListResponseSerializer, many=True, http_status=status.HTTP_200_OK)
        return _serialize_and_respond(todos, TodoGetResponseSerializer, many=True, http_status=status.HTTP_200_OK)

    # POST /todo/
    req_serializer = TodoCreateRequestSerializer(data=request.data)
    if not req_serializer.is_valid():
        return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    validated = req_serializer.validated_data

    # Build dataclass explicitly (don't rely on serializer having to_dataclass)
    todo_dto = TodoData(
        title=validated.get('title'),
        description=validated.get('description', ""),
        completed=validated.get('completed', False),
    )

    # create_todo currently returns an id in your code — preserve that behaviour
    created = todo_service.create_todo(todo_dto)

    # If service returned a model instance or dict, serialize it.
    if isinstance(created, dict) or not isinstance(created, int):
        # assume created is an object/dict representing the created resource
        return _serialize_and_respond(created, TodoCreateResponseSerializer, many=False, http_status=status.HTTP_201_CREATED)

    # fallback: service returned id
    return Response({'id': created, 'message': 'Created'}, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def todo_detail(request, id):
    # GET /todo/<id>/
    if request.method == 'GET':
        todo = todo_service.get_todo(id)  # might be a dict or model instance
        if not todo:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
        return _serialize_and_respond(todo, TodoGetResponseSerializer, many=False)

    # PUT /todo/<id>/
    if request.method == 'PUT':
        existing = todo_service.get_todo(id)
        if not existing:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        # Partial True semantics: accept partial updates
        req_serializer = TodoUpdateRequestSerializer(data=request.data, partial=True)
        if not req_serializer.is_valid():
            return Response(req_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        validated = req_serializer.validated_data

        # Build a TodoData for update. We want missing fields to remain unchanged.
        # We'll populate missing fields from existing (which may be dict or model instance).
        # Attempt to convert existing to a dict safely:
        if isinstance(existing, dict):
            existing_dict = existing
        else:
            # model instance -> build a dict
            existing_dict = {
                'title': getattr(existing, 'title', None),
                'description': getattr(existing, 'description', None),
                'completed': getattr(existing, 'completed', None),
            }

        # Merge: if field provided in validated, use it; otherwise use existing value
        merged = {
            'title': validated.get('title', existing_dict.get('title')),
            'description': validated.get('description', existing_dict.get('description')),
            'completed': validated.get('completed', existing_dict.get('completed')),
        }

        todo_dto = TodoData(
            title=merged['title'],
            description=merged['description'],
            completed=merged['completed'],
        )

        updated = todo_service.update_todo(id, todo_dto)
        # updated may be True/False or model/dict — handle both
        if updated is False or updated is None:
            return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)

        if isinstance(updated, (dict, object)) and not isinstance(updated, bool):
            # If service returned the updated object, serialize & return it
            return _serialize_and_respond(updated, TodoUpdateResponseSerializer, many=False)
        return Response({'message': 'Updated'}, status=status.HTTP_200_OK)

    # DELETE /todo/<id>/
    deleted = todo_service.delete_todo(id)
    if not deleted:
        return Response({'error': 'Not found'}, status=status.HTTP_404_NOT_FOUND)
    return Response({'message': 'Deleted'}, status=status.HTTP_200_OK)
