from rest_framework import serializers


class SongCreateRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    artist = serializers.CharField(max_length=255)
    duration = serializers.IntegerField(min_value=1)
    release_date = serializers.DateField()
