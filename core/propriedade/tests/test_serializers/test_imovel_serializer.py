import logging

import pytest
from django.forms import model_to_dict

from core.propriedade.api.serializers.imovel_serializer import ImovelGetSerializer
from core.propriedade.api.serializers.imovel_serializer import ImovelPostSerializer

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestImovelSerializer:
    def test_create_imovel_post_serializer(
        self,
        imovel_factory,
        cidade_factory,
        proprietario_factory,
        tipo_de_imovel_factory,
    ):
        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()
        imovel_data = model_to_dict(imovel)

        logger.info("imovel_data: %s", imovel_data)
        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        serializer = ImovelPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        imovel = serializer.save()
        assert imovel, serializer.errors
        assert imovel.titulo == imovel_data.get("titulo"), "deveria ser igual"
        assert imovel.tipo_de_contrato == imovel_data.get(
            "tipo_de_contrato"
        ), "deveria ser igual"

    def test_read_imovel_get_serializer(self, imovel_factory):
        imovel = imovel_factory()

        serializer = ImovelGetSerializer
        serializer = serializer(imovel)

        assert serializer.data.get("pais") == imovel.pais, "deveria ser igual"
