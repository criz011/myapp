from rest_framework import serializers
from .get import TodoGetResponseSerializer

class TodoListResponseSerializer(serializers.Serializer):
    results = TodoGetResponseSerializer(many=True)
    count = serializers.IntegerField()
