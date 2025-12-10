from .models import Todo
from .dataclass.todo_dto import TodoData
from typing import Optional, List, Dict, Any

def list_todos() -> List[Dict[str, Any]]:
    qs = Todo.objects.all().values('id', 'title', 'description', 'completed')
    return [dict(x) for x in qs]

def get_todo(todo_id: int) -> Optional[Dict[str, Any]]:
    t = Todo.objects.filter(id=todo_id).values('id', 'title', 'description', 'completed').first()
    return dict(t) if t else None

def create_todo(todo_data: TodoData) -> int:
    todo = Todo.objects.create(
        title=todo_data.title,
        description=todo_data.description,
        completed=todo_data.completed
    )
    return todo.id

def update_todo(todo_id: int, todo_data: TodoData) -> bool:
    updated = Todo.objects.filter(id=todo_id).update(
        title=todo_data.title,
        description=todo_data.description,
        completed=todo_data.completed
    )
    return bool(updated)

def delete_todo(todo_id: int) -> bool:
    deleted, _ = Todo.objects.filter(id=todo_id).delete()
    return bool(deleted)
