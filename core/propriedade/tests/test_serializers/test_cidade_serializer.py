import logging

import pytest
from django.forms import model_to_dict

from core.propriedade.api.serializers.cidade_serializer import CidadeGetSerializer
from core.propriedade.api.serializers.cidade_serializer import CidadePostSerializer

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestCidadeSerializer:
    def test_create_cidade_post_serializer(self, cidade_factory, estado_factory):
        cidade = cidade_factory.build()
        cidade_data = model_to_dict(cidade)

        estado = estado_factory()

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        serializer = CidadePostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        cidade = serializer.save()
        assert cidade, serializer.errors
        assert cidade.nome == cidade_data.get("nome"), "deveria ser igual"

    def test_read_cidade_get_serializer(self, cidade_factory):
        cidade = cidade_factory()

        serializer = CidadeGetSerializer
        serializer = serializer(cidade)

        assert serializer.data.get("nome") == cidade.nome, "deveria ser igual"
