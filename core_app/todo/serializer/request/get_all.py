from rest_framework import serializers

class TodoListRequestSerializer(serializers.Serializer):
    completed = serializers.BooleanField(required=False)
    limit = serializers.IntegerField(required=False, min_value=1)
    offset = serializers.IntegerField(required=False, min_value=0)
