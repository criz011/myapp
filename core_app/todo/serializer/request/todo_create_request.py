from rest_framework import serializers
from ...dataclass.todo_dto import TodoData

class TodoCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)

    def to_dataclass(self) -> TodoData:
        return TodoData.from_dict(self.validated_data)
