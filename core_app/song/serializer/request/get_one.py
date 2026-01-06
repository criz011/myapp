from rest_framework import serializers


class SongGetOneRequestSerializer(serializers.Serializer):
    id = serializers.IntegerField(required=True)
