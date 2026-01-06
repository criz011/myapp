from rest_framework import serializers


class SongCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    duration = serializers.IntegerField()
    release_date = serializers.DateField()
    artist_id = serializers.IntegerField()