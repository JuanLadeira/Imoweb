import logging

import pytest
from rest_framework.test import APIRequestFactory

from core.propriedade.api.serializers.imovel_serializer import ImovelGetSerializer
from core.propriedade.api.serializers.imovel_serializer import ImovelPostSerializer
from core.propriedade.api.views.imovel_viewset import ImovelViewSet

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("method", "expected_serializer"),
    [
        ("GET", ImovelGetSerializer),
        ("POST", ImovelPostSerializer),
        ("PUT", ImovelPostSerializer),
        ("PATCH", ImovelPostSerializer),
    ],
)
def test_get_serializer_class(method, expected_serializer):
    factory = APIRequestFactory()

    if method == "GET":
        request = factory.get("/")
    elif method == "POST":
        request = factory.post("/")
    elif method == "PUT":
        request = factory.put("/")
    elif method == "PATCH":
        request = factory.patch("/")

    view = ImovelViewSet()
    view.request = request

    serializer = view.get_serializer_class()

    assert (
        serializer == expected_serializer
    ), f"Expected {expected_serializer} serializer, but got {serializer}"
