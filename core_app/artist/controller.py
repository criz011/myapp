from rest_framework.decorators import api_view
from rest_framework.request import Request

from core_app.artist.views import ArtistView
from core_app.common.decorators.validate_serializer import validate_serializer

from core_app.artist.serializer.request.create import ArtistCreateRequestSerializer
from core_app.artist.serializer.request.get_one import ArtistGetOneRequestSerializer
from core_app.artist.serializer.request.get_all import ArtistGetAllRequestSerializer
from core_app.artist.serializer.request.update import ArtistUpdateRequestSerializer
from core_app.common.serializer.id_request import IdRequestSerializer


class ArtistController:
    view = ArtistView()

    @staticmethod
    @api_view(["POST"])
    @validate_serializer(ArtistCreateRequestSerializer)
    def create(request: Request, params):
        return ArtistController.view.create_artist(params)

    @staticmethod
    @api_view(["GET"])
    @validate_serializer(ArtistGetAllRequestSerializer, source="query")
    def get_all(request: Request, params):
        return ArtistController.view.get_all(params)

    @staticmethod
    @api_view(["GET"])
    @validate_serializer(ArtistGetOneRequestSerializer, source="query")
    def get_one(request: Request, params):
        return ArtistController.view.get_one(params["id"])

    @staticmethod
    @api_view(["PUT"])
    @validate_serializer(IdRequestSerializer)
    @validate_serializer(ArtistUpdateRequestSerializer)
    def update(request: Request, update_params, id_params):
        return ArtistController.view.update_artist(
            id_params["id"],
            update_params
        )

    @staticmethod
    @api_view(["DELETE"])
    @validate_serializer(IdRequestSerializer, source="query")
    def delete(request: Request, params):
        return ArtistController.view.delete_artist(params["id"])
