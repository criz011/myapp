from rest_framework import serializers

class TodoGetRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField()
