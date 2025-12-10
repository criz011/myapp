from rest_framework import serializers
from dataclasses import asdict
from ...dataclass.todo_dto import TodoData

class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(required=False, allow_blank=True)
    completed = serializers.BooleanField(required=False)

    def to_dataclass(self, existing: TodoData = None) -> TodoData:
        base = asdict(existing) if existing else {}
        merged = {**base, **self.validated_data}
        return TodoData.from_dict(merged)
