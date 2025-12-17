from rest_framework.response import Response
from rest_framework import status
from typing import Any, Optional


class ResponseUtils:

    @staticmethod
    def success(
        message: str,
        data: Optional[Any] = None,
        status_code: int = status.HTTP_200_OK
    ) -> Response:
        response = {
            "success": True,
            "message": message
        }

        if data is not None:
            response["data"] = data

        return Response(response, status=status_code)

    @staticmethod
    def error(
        message: str,
        errors: Optional[Any] = None,
        status_code: int = status.HTTP_400_BAD_REQUEST
    ) -> Response:
        response = {
            "success": False,
            "message": message
        }

        if errors is not None:
            response["errors"] = errors

        return Response(response, status=status_code)
