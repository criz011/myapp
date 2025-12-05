import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from . import views as todo_service


@csrf_exempt
def todo_list(request):
    if request.method == "GET":
        todos = todo_service.list_todos()
        return JsonResponse(todos, safe=False)

    if request.method == "POST":
        data = json.loads(request.body)
        todo_id = todo_service.create_todo(data)
        return JsonResponse({"id": todo_id, "message": "Created"}, status=201)

    return JsonResponse({"error": "Method not allowed"}, status=405)


@csrf_exempt
def todo_detail(request, id):
    if request.method == "GET":
        todo = todo_service.get_todo(id)
        if not todo:
            return JsonResponse({"error": "Not found"}, status=404)
        return JsonResponse(todo)

    if request.method == "PUT":
        data = json.loads(request.body)
        updated = todo_service.update_todo(id, data)
        if not updated:
            return JsonResponse({"error": "Not found"}, status=404)
        return JsonResponse({"message": "Updated"})

    if request.method == "DELETE":
        deleted = todo_service.delete_todo(id)
        if not deleted:
            return JsonResponse({"error": "Not found"}, status=404)
        return JsonResponse({"message": "Deleted"})

    return JsonResponse({"error": "Method not allowed"}, status=405)
