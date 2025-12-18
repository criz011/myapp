from rest_framework import serializers

class IdRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
