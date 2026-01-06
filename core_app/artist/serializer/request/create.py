from rest_framework import serializers


class ArtistCreateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(min_value=1)
