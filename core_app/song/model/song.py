from django.db import models
from core_app.artist.model.artist import Artist

class Song(models.Model):
    title = models.CharField(max_length=255)
    duration = models.IntegerField()
    release_date = models.DateField()

    artist = models.ForeignKey(
        Artist,
        on_delete=models.PROTECT,
        related_name="songs"
    )

    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "songs"
        ordering = ["-created_at"]

    def __str__(self) -> str:
        return f"{self.title} - {self.artist}"


    @staticmethod
    def create_song(
        title,
        artist,
        duration,
        release_date,
        is_active=True
    ):
        return Song.objects.create(
            title=title,
            artist=artist,
            duration=duration,
            release_date=release_date,
            is_active=is_active
        )

    @staticmethod
    def get_all(params=None):
        qs = Song.objects.filter(is_active=True)

        if not params:
            return qs

        try:
            page_num = int(params.get("page_num", 1))
            limit = int(params.get("limit", 10))
        except ValueError:
            page_num = 1
            limit = 10

        if page_num < 1:
            page_num = 1
        if limit < 1:
            limit = 10

        start = (page_num - 1) * limit
        end = start + limit

        return qs[start:end]


    @staticmethod
    def get_one(song_id):
        return Song.objects.filter(id=song_id, is_active=True).first()

    @staticmethod
    def update_song(
        song_id,
        title=None,
        artist=None,
        duration=None,
        release_date=None,
        is_active=None
    ):
        song = Song.objects.filter(id=song_id).first()
        if not song:
            return None

        if title is not None:
            song.title = title
        if artist is not None:
            song.artist = artist
        if duration is not None:
            song.duration = duration
        if release_date is not None:
            song.release_date = release_date
        if is_active is not None:
            song.is_active = is_active

        song.save()
        return song

    @staticmethod
    def delete_one(song_id):
        song = Song.objects.filter(id=song_id).first()
        if not song:
            return False
        song.delete()
        return True

    @staticmethod
    def get_count():
        return Song.objects.filter(is_active=True).count()

