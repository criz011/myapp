from django.db import models


class Artist(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "artist"

    @staticmethod
    def create_artist(**kwargs):
        return Artist.objects.create(**kwargs)

    @staticmethod
    def get_one(artist_id):
        return Artist.objects.filter(id=artist_id, is_active=True).first()
