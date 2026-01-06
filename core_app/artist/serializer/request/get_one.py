from rest_framework import serializers


class ArtistGetOneRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
