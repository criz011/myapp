from rest_framework import serializers


class ArtistResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()
    age = serializers.IntegerField()
    created_at = serializers.DateTimeField()
