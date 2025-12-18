from django.db import models


class Todo(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "todo_todo"
        ordering = ["-created_at"]

    def __str__(self):
        return self.title

    @staticmethod
    def create_todo(title, description="", completed=False):
        return Todo.objects.create(
            title=title,
            description=description,
            completed=completed
        )

    @staticmethod
    def get_all(params=None):
        qs = Todo.objects.all()

        if not params:
            return qs

        try:
            page_num = int(params.get("page_num", 1))
            limit = int(params.get("limit", 10))
        except ValueError:
            page_num = 1
            limit = 10

        if page_num < 1:
            page_num = 1
        if limit < 1:
            limit = 10

        start = (page_num - 1) * limit
        end = start + limit

        return qs[start:end]

    @staticmethod
    def get_count():
        return Todo.objects.count()

    @staticmethod
    def get_one(todo_id):
        return Todo.objects.filter(id=todo_id).first()

    @staticmethod
    def update_todo(
        todo_id,
        title=None,
        description=None,
        completed=None
    ):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return None

        if title is not None:
            todo.title = title
        if description is not None:
            todo.description = description
        if completed is not None:
            todo.completed = completed

        todo.save()
        return todo

    @staticmethod
    def delete_one(todo_id):
        todo = Todo.objects.filter(id=todo_id).first()
        if not todo:
            return False

        todo.delete()
        return True
