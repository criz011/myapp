from functools import wraps


def validate_serializer(serializer_class, source="body"):
    """
    Common decorator to validate request data using a serializer.

    :param serializer_class: DRF serializer class
    :param source: 'body' | 'query'
    """

    def decorator(func):
        @wraps(func)
        def wrapper(request, *args, **kwargs):
            if source == "query":
                data = request.query_params
            else:
                data = request.data

            serializer = serializer_class(data=data)
            serializer.is_valid(raise_exception=True)

            # pass validated data to the controller method
            return func(request, serializer.validated_data, *args, **kwargs)

        return wrapper

    return decorator
