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
                data=self._serialize_song(song)
            )
        )

    def get_song(self, song_id: Optional[int] = None, params=None):
        # -------- GET ONE --------
        if song_id:
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
                    data=[self._serialize_song(song)]
                )
            )

        # -------- GET ALL (PAGINATED) --------
        songs = Song.get_all(params)
        data = [self._serialize_song(s) for s in songs]

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
                data=self._serialize_song(song)
            )
        )

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

    # -------- SERIALIZER --------
    @staticmethod
    def _serialize_song(song):
        return SongResponseSerializer(song).data
