from .models import Todo

def list_todos():
    return list(Todo.objects.values())

def get_todo(todo_id):
    return Todo.objects.filter(id=todo_id).values().first()

def create_todo(data):
    todo = Todo.objects.create(
        title=data.get("title"),
        description=data.get("description", ""),
        completed=data.get("completed", False)
    )
    return todo.id

def update_todo(todo_id, data):
    return Todo.objects.filter(id=todo_id).update(
        title=data.get("title"),
        description=data.get("description"),
        completed=data.get("completed"),
    )

def delete_todo(todo_id):
    deleted, _ = Todo.objects.filter(id=todo_id).delete()
    return deleted
