from rest_framework import serializers

class TodoResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(allow_blank=True)
    completed = serializers.BooleanField()
