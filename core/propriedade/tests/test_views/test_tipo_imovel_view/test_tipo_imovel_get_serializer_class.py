import logging

import pytest
from rest_framework.test import APIRequestFactory

from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelGetSerializer,
)
from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelPostSerializer,
)
from core.propriedade.api.views.tipo_imovel_viewset import TipoDeImovelViewSet

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("method", "expected_serializer"),
    [
        ("GET", TipoDeImovelGetSerializer),
        ("POST", TipoDeImovelPostSerializer),
        ("PUT", TipoDeImovelPostSerializer),
        ("PATCH", TipoDeImovelPostSerializer),
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

    view = TipoDeImovelViewSet()
    view.request = request

    serializer = view.get_serializer_class()

    assert serializer == expected_serializer
