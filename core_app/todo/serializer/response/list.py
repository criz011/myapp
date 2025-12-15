from rest_framework import serializers
from .todo import TodoResponseSerializer

class TodoListResponseSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    results = TodoResponseSerializer(many=True)
