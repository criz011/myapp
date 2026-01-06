from rest_framework.response import Response

from core_app.artist.model.artist import Artist
from core_app.artist.dataclass.request.create_artist import CreateArtistRequest
from core_app.artist.dataclass.request.update_artist import UpdateArtistRequest
from core_app.common.utils import Utils
from core_app.artist.serializer.response.artist_response import ArtistResponseSerializer


class ArtistView:
    artist_created = "Artist created successfully"
    artist_updated = "Artist updated successfully"
    artist_deleted = "Artist deleted successfully"

    # -------- CREATE --------
    def create_artist(self, params):
        req = CreateArtistRequest(**params)

        artist = Artist.objects.create(
            name=req.name,
            age=req.age
        )

        return Response(
            Utils.success_response(
                message=self.artist_created,
                data=ArtistResponseSerializer(artist).data
            )
        )

    # -------- GET ONE --------
    def get_one(self, artist_id: int):
        artist = Artist.objects.filter(id=artist_id, is_active=True).first()

        if not artist:
            return Response(
                Utils.error_response(
                    message="Artist not found",
                    error="INVALID_ID"
                )
            )

        return Response(
            Utils.success_response(
                message="Artist fetched successfully",
                data=ArtistResponseSerializer(artist).data
            )
        )

    # -------- GET ALL --------
    def get_all(self, params=None):
        artists = Artist.objects.filter(is_active=True)

        data = ArtistResponseSerializer(artists, many=True).data

        return Response(
            Utils.success_response(
                message="Artists fetched successfully",
                data=data
            )
        )

    # -------- UPDATE --------
    def update_artist(self, artist_id: int, params):
        req = UpdateArtistRequest(**params)

        artist = Artist.objects.filter(id=artist_id, is_active=True).first()
        if not artist:
            return Response(
                Utils.error_response(
                    message="Artist not found",
                    error="INVALID_ID"
                )
            )

        if req.name is not None:
            artist.name = req.name
        if req.age is not None:
            artist.age = req.age

        artist.save()

        return Response(
            Utils.success_response(
                message=self.artist_updated,
                data=ArtistResponseSerializer(artist).data
            )
        )

    # -------- DELETE --------
    def delete_artist(self, artist_id: int):
        artist = Artist.objects.filter(id=artist_id, is_active=True).first()
        if not artist:
            return Response(
                Utils.error_response(
                    message="Artist not found",
                    error="INVALID_ID"
                )
            )

        artist.is_active = False
        artist.save()

        return Response(
            Utils.success_response(
                message=self.artist_deleted
            )
        )
