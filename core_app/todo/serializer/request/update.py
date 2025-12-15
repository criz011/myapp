from rest_framework import serializers

class TodoUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    description = serializers.CharField(allow_blank=True, required=False, allow_null=True)
    completed = serializers.BooleanField(required=False)
