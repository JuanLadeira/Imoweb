from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateCidadeEndpoint:
    endpoint = "/api/propriedades/cidades/"

    @classmethod
    def get_endpoint(cls, cidade_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            cidade_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """

        if cidade_id:
            return f"{cls.endpoint}{cidade_id}/"
        return cls.endpoint

    def test_agente_super_user_update_agentes(
        self, agente_logado, cidade_factory, estado_factory
    ):
        """
        test_agente_super_user_update_agentes

        Testa a atualização de agentes por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        cidade = cidade_factory()
        cidade_update = cidade_factory.build()
        cidade_data = model_to_dict(cidade_update)
        estado = estado_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(cidade.id)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_agentes(self, agente_logado, cidade_factory, estado_factory):
        """
        test_agente_update_agentes

        Testa a atualização de agentes por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        cidade = cidade_factory()
        cidade_update = cidade_factory.build()
        cidade_data = model_to_dict(cidade_update)
        estado = estado_factory()
        url = self.get_endpoint(cidade.id)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_agentes(
        self, proprietario_logado, cidade_factory, estado_factory
    ):
        """
        Testa a atualização de agentes por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            cidade_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        cidade = cidade_factory()
        cidade_update = cidade_factory.build()
        cidade_data = model_to_dict(cidade_update)
        estado = estado_factory()

        url = self.get_endpoint(cidade.id)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_agentes(
        self,
        inquilino_logado,
        cidade_factory,
        estado_factory,
    ):
        """
        test_inquilino_update_agentes

        Testa a atualização de agentes por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            cidade_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        cidade = cidade_factory()
        cidade_update = cidade_factory.build()
        cidade_data = model_to_dict(cidade_update)
        estado = estado_factory()
        url = self.get_endpoint(cidade.id)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
