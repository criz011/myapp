from rest_framework import serializers

class TodoDeleteManyRequestSerializer(serializers.Serializer):
    ids = serializers.ListField(
        child=serializers.IntegerField(), allow_empty=False
    )
