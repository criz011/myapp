from rest_framework import serializers


class SongGetAllRequestSerializer(serializers.Serializer):
    page_num = serializers.IntegerField(required=False, default=1, min_value=1)
    limit = serializers.IntegerField(required=False, default=10, min_value=1)
