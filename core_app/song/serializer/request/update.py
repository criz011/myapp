from rest_framework import serializers

class SongUpdateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255, required=False)
    artist = serializers.CharField(max_length=255, required=False)
    duration = serializers.IntegerField(min_value=1, required=False)
    release_date = serializers.DateField(required=False)
