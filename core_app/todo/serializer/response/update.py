from rest_framework import serializers

class TodoUpdateResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    description = serializers.CharField()
    completed = serializers.BooleanField()
