from rest_framework import serializers

class SongResponseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    duration = serializers.IntegerField()
    release_date = serializers.DateField()
    is_active = serializers.BooleanField()
    created_at = serializers.DateTimeField()

    artist = serializers.SerializerMethodField()

    def get_artist(self, obj):
        return {
            "id": obj.artist.id,
            "name": obj.artist.name,
            "age": obj.artist.age
        }
