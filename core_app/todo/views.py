from typing import Optional

from rest_framework import status

from .model import Todo
from .dataclass.todo_dto import TodoData
from core_app.common.utils import ResponseUtils


class TodoView:
    data_created = "Todo created successfully"
    data_updated = "Todo updated successfully"
    data_deleted = "Todo deleted successfully"

    def create_todo(self, params):
        todo_data = TodoData(**params)

        todo = Todo.objects.create(
            title = todo_data.title,
            description = todo_data.description,
            completed = todo_data.completed
        )

        return ResponseUtils.success(
            message=self.data_created,
            data={
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "completed": todo.completed,
            },
            status_code=status.HTTP_201_CREATED
        )

    def get_todo(self, todo_id: Optional[int] = None):
        if todo_id:
            todos = Todo.objects.filter(id=todo_id)
            if not todos.exists():
                return ResponseUtils.error(
                    message = f"Todo with id {todo_id} not found",
                    status_code = status.HTTP_404_NOT_FOUND
                )
        else:
            todos = Todo.objects.all()

        data = [
            {
                "id": t.id,
                "title": t.title,
                "description": t.description,
                "completed": t.completed,
            }
            for t in todos
        ]

        return ResponseUtils.success(
            message="Todos fetched successfully",
            data=data,
            status_code=status.HTTP_200_OK
        )

    def update_todo(self, todo_id: int, params):
        try:
            todo = Todo.objects.get(id=todo_id)
        except Todo.DoesNotExist:
            return ResponseUtils.error(
                message=f"Todo with id {todo_id} not found",
                status_code=status.HTTP_404_NOT_FOUND
            )

        for key, value in params.items():
            setattr(todo, key, value)

        todo.save()

        return ResponseUtils.success(
            message=self.data_updated,
            data={
                "id": todo.id,
                "title": todo.title,
                "description": todo.description,
                "completed": todo.completed,
            },
            status_code=status.HTTP_200_OK
        )

    def delete_todo(self, todo_id: int):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return ResponseUtils.error(
                message="Todo not found",
                status_code=status.HTTP_404_NOT_FOUND
            )

        todo.delete()

        return ResponseUtils.success(
            message=self.data_deleted,
            status_code=status.HTTP_200_OK
        )
