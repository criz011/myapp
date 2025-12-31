from rest_framework import serializers

class SongResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    artist = serializers.CharField()
    duration = serializers.IntegerField()
    release_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()
