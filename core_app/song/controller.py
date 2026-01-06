from rest_framework.decorators import api_view
from rest_framework.request import Request

from core_app.song.views import SongView
from core_app.common.decorators.validate_serializer import validate_serializer

from core_app.song.serializer.request.create import SongCreateRequestSerializer
from core_app.song.serializer.request.update import SongUpdateRequestSerializer
from core_app.song.serializer.request.get_all import SongGetAllRequestSerializer
from core_app.song.serializer.request.get_one import SongGetOneRequestSerializer
from core_app.common.serializer.id_request import IdRequestSerializer


class SongController:

    view = SongView()

    @staticmethod
    @api_view(["POST"])
    @validate_serializer(SongCreateRequestSerializer)
    def create(request, params):
        return SongController.view.create_song(params)

    @staticmethod
    @api_view(["GET"])
    @validate_serializer(SongGetAllRequestSerializer, source="query")
    def get_all(request, params):
        return SongController.view.get_all(params)

    @staticmethod
    @api_view(["GET"])
    @validate_serializer(SongGetOneRequestSerializer, source="query")
    def get_one(request, params):
        return SongController.view.get_one(params["id"])

    @staticmethod
    @api_view(["PUT"])
    @validate_serializer(IdRequestSerializer)
    @validate_serializer(SongUpdateRequestSerializer)
    def update(request, update_params, id_params):
        return SongController.view.update_song(id_params["id"],update_params)

    @staticmethod
    @api_view(["DELETE"])
    @validate_serializer(IdRequestSerializer, source="query")
    def delete(request, params):
        return SongController.view.delete_song(params["id"])
