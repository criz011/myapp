from rest_framework import serializers


class ArtistUpdateRequestSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=255, required=False)
    age = serializers.IntegerField(required=False, min_value=1)
