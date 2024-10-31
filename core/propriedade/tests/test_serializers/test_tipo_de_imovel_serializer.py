import logging

import pytest
from django.forms import model_to_dict

from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelGetSerializer,
)
from core.propriedade.api.serializers.tipo_de_imovel_serializer import (
    TipoDeImovelPostSerializer,
)

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestTipoDeImovelSerializer:
    def test_create_tipo_de_imovel_post_serializer(self, tipo_de_imovel_factory):
        tipo_de_imovel = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        serializer = TipoDeImovelPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        tipo_de_imovel = serializer.save()
        assert tipo_de_imovel, serializer.errors
        assert tipo_de_imovel.nome == tipo_de_imovel_data.get(
            "nome"
        ), "deveria ser igual"
        assert tipo_de_imovel.tipo == tipo_de_imovel_data.get(
            "tipo"
        ), "deveria ser igual"

    def test_read_tipo_de_imovel_get_serializer(self, tipo_de_imovel_factory):
        tipo_de_imovel = tipo_de_imovel_factory()

        serializer = TipoDeImovelGetSerializer
        serializer = serializer(tipo_de_imovel)

        assert serializer.data.get("nome") == tipo_de_imovel.nome, "deveria ser igual"
