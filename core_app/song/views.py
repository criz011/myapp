from typing import Optional
from rest_framework.response import Response

from .model import Song
from .dataclass.song_dto import SongData
from core_app.common.utils import Utils
from core_app.song.serializer.response.song_response import SongResponseSerializer


class SongView:
    song_created = "Song created successfully"
    song_updated = "Song updated successfully"
    song_deleted = "Song deleted successfully"

    # -------- CREATE --------
    def create_song(self, params):
        song_data = SongData(**params)

        song = Song.create_song(
            title=song_data.title,
            artist=song_data.artist,
            duration=song_data.duration,
            release_date=song_data.release_date
        )

        return Response(
            Utils.success_response(
                message=self.song_created,
                data=SongResponseSerializer(song).data
            )
        )

    # -------- GET ONE --------
    def get_one(self, song_id: int):
        song = Song.get_one(song_id)

        if not song:
            return Response(
                Utils.error_response(
                    message="Song not found",
                    error="INVALID_ID"
                )
            )

        return Response(
            Utils.success_response(
                message="Song fetched successfully",
                data=SongResponseSerializer(song).data
            )
        )

    # -------- GET ALL --------
    def get_all(self, params=None):
        songs = Song.get_all(params)

        data = SongResponseSerializer(songs, many=True).data

        total = Song.get_count()
        page_num = int(params.get("page_num", 1)) if params else 1
        limit = int(params.get("limit", 10)) if params else 10

        return Response(
            Utils.success_response(
                message="Songs fetched successfully",
                data=data,
                meta={
                    "total": total,
                    "page_num": page_num,
                    "limit": limit
                }
            )
        )

    # -------- UPDATE --------
    def update_song(self, song_id: int, params):
        song = Song.update_song(song_id, **params)

        if not song:
            return Response(
                Utils.error_response(
                    message="Song not found",
                    error="INVALID_ID"
                )
            )

        return Response(
            Utils.success_response(
                message=self.song_updated,
                data=SongResponseSerializer(song).data
            )
        )

    # -------- DELETE --------
    def delete_song(self, song_id: int):
        deleted = Song.delete_one(song_id)

        if not deleted:
            return Response(
                Utils.error_response(
                    message="Song not found",
                    error="INVALID_ID"
                )
            )

        return Response(
            Utils.success_response(
                message=self.song_deleted
            )
        )