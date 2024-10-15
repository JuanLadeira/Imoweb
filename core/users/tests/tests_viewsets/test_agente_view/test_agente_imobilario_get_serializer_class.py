import pytest
from rest_framework.test import APIRequestFactory

from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioGetSerializer,
)
from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioPostSerializer,
)
from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioUpdateSerializer,
)
from core.users.api.views.agente_imobilario_viewset import AgenteImobiliarioViewSet


@pytest.mark.parametrize(
    ("method", "expected_serializer"),
    [
        ("GET", AgenteImobiliarioGetSerializer),
        ("POST", AgenteImobiliarioPostSerializer),
        ("PUT", AgenteImobiliarioUpdateSerializer),
        ("PATCH", AgenteImobiliarioUpdateSerializer),
    ],
)
@pytest.mark.django_db()
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

    view = AgenteImobiliarioViewSet()
    view.request = request

    serializer = view.get_serializer_class()

    assert serializer == expected_serializer
