import pytest
from rest_framework.test import APIRequestFactory

from core.users.api.serializers.inquilino_serializer import InquilinoGetSerializer
from core.users.api.serializers.inquilino_serializer import InquilinoPostSerializer
from core.users.api.serializers.inquilino_serializer import InquilinoUpdateSerializer
from core.users.api.views.inquilino_viewset import InquilinoViewSet


@pytest.mark.parametrize(
    ("method", "expected_serializer"),
    [
        ("GET", InquilinoGetSerializer),
        ("POST", InquilinoPostSerializer),
        ("PUT", InquilinoUpdateSerializer),
        ("PATCH", InquilinoUpdateSerializer),
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

    view = InquilinoViewSet()
    view.request = request

    assert view.get_serializer_class() == expected_serializer
