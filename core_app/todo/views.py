from typing import Optional

from .model import Todo
from .dataclass.todo_dto import TodoData
from core_app.common.utils import Utils


class TodoView:
    data_created = "Todo created successfully"
    data_updated = "Todo updated successfully"
    data_deleted = "Todo deleted successfully"

    def create_todo(self, params):
        todo_data = TodoData(**params)

        todo = Todo.create_todo(
            title=todo_data.title,
            description=todo_data.description,
            completed=todo_data.completed
        )

        return Utils.success_response(
            message=self.data_created,
            data=self._serialize_todo(todo)
        )

    def get_todo(self, todo_id: Optional[int] = None, params=None):
        # -------- GET ONE --------
        if todo_id:
            todo = Todo.get_one(todo_id)
            if not todo:
                return Utils.error_response(
                    message="Todo not found",
                    error="INVALID_ID"
                )

            return Utils.success_response(
                message="Todo fetched successfully",
                data=[self._serialize_todo(todo)]
            )

        # -------- GET ALL (PAGINATED) --------
        todos = Todo.get_all(params)
        data = [self._serialize_todo(t) for t in todos]

        total = Todo.get_count()
        page_num = int(params.get("page_num", 1)) if params else 1
        limit = int(params.get("limit", 10)) if params else 10

        return Utils.success_response(
            message="Todos fetched successfully",
            data=data,
            meta={
                "total": total,
                "page_num": page_num,
                "limit": limit
            }
        )

    def update_todo(self, todo_id: int, params):
        todo = Todo.update_todo(todo_id, **params)

        if not todo:
            return Utils.error_response(
                message="Todo not found",
                error="INVALID_ID"
            )

        return Utils.success_response(
            message=self.data_updated,
            data=self._serialize_todo(todo)
        )

    def delete_todo(self, todo_id: int):
        deleted = Todo.delete_one(todo_id)

        if not deleted:
            return Utils.error_response(
                message="Todo not found",
                error="INVALID_ID"
            )

        return Utils.success_response(
            message=self.data_deleted
        )

    # -------- INTERNAL SERIALIZER --------
    @staticmethod
    def _serialize_todo(todo):
        return {
            "id": todo.id,
            "title": todo.title,
            "description": todo.description,
            "completed": todo.completed,
            "created_at": todo.created_at,
        }
