import logging

import pytest
from django.forms import model_to_dict

from core.propriedade.api.serializers.estado_serializer import EstadoGetSerializer
from core.propriedade.api.serializers.estado_serializer import EstadoPostSerializer

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestEstadoSerializer:
    def test_create_estado_post_serializer(self, estado_factory):
        estado = estado_factory.build()
        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        serializer = EstadoPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        estado = serializer.save()
        assert estado, serializer.errors
        assert estado.nome == estado_data.get("nome"), "deveria ser igual"
        assert estado.uf == estado_data.get("uf"), "deveria ser igual"

    def test_read_estado_get_serializer(self, estado_factory):
        estado = estado_factory()

        serializer = EstadoGetSerializer
        serializer = serializer(estado)

        assert serializer.data.get("nome") == estado.nome, "deveria ser igual"
