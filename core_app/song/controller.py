from rest_framework.decorators import api_view
from rest_framework.request import Request

from core_app.song.views import SongView
from core_app.song.serializer.request.create import SongCreateRequestSerializer
from core_app.song.serializer.request.update import SongUpdateRequestSerializer
from core_app.common.serializer.id_request import IdRequestSerializer


class SongController:

    view = SongView()

    @staticmethod
    @api_view(["POST"])
    def create(request: Request):
        serializer = SongCreateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return SongController.view.create_song(serializer.validated_data)

    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        return SongController.view.get_song(params=request.query_params)

    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        serializer = IdRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return SongController.view.get_song(serializer.validated_data["id"])

    @staticmethod
    @api_view(["PUT"])
    def update(request: Request):
        id_serializer = IdRequestSerializer(data=request.data)
        id_serializer.is_valid(raise_exception=True)

        serializer = SongUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return SongController.view.update_song(
            id_serializer.validated_data["id"],
            serializer.validated_data
        )

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        serializer = IdRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        return SongController.view.delete_song(serializer.validated_data["id"])
