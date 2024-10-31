import logging

import pytest
from rest_framework.test import APIRequestFactory

from core.users.api.serializers.proprietario_serializer import ProprietarioGetSerializer
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioPostSerializer,
)
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioUpdateSerializer,
)
from core.users.api.views.proprietario_viewset import ProprietarioViewSet

logger = logging.getLogger(__name__)


@pytest.mark.parametrize(
    ("method", "expected_serializer"),
    [
        ("GET", ProprietarioGetSerializer),
        ("POST", ProprietarioPostSerializer),
        ("PUT", ProprietarioUpdateSerializer),
        ("PATCH", ProprietarioUpdateSerializer),
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

    view = ProprietarioViewSet()
    view.request = request

    serializer = view.get_serializer_class()

    assert serializer == expected_serializer
