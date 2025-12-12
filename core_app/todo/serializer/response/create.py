from rest_framework import serializers

class TodoCreateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()
