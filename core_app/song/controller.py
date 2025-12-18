from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

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
        result = SongController.view.create_song(serializer.validated_data)
        return Response(result)

    @staticmethod
    @api_view(["GET"])
    def get_all(request: Request):
        result = SongController.view.get_song(params=request.query_params)
        return Response(result)

    @staticmethod
    @api_view(["GET"])
    def get_one(request: Request):
        serializer = IdRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = SongController.view.get_song(serializer.validated_data["id"])
        return Response(result)

    @staticmethod
    @api_view(["PUT"])
    def update(request: Request):
        id_serializer = IdRequestSerializer(data=request.data)
        id_serializer.is_valid(raise_exception=True)

        serializer = SongUpdateRequestSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        result = SongController.view.update_song(
            id_serializer.validated_data["id"],
            serializer.validated_data
        )
        return Response(result)

    @staticmethod
    @api_view(["DELETE"])
    def delete(request: Request):
        serializer = IdRequestSerializer(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        result = SongController.view.delete_song(serializer.validated_data["id"])
        return Response(result)
