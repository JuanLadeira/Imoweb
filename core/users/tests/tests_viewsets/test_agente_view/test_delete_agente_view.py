from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestdeleteAgenteEndpoint:
    endpoint = "/api/users/agentes/"

    @classmethod
    def get_endpoint(cls, agente_imobiliario_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            agente_imobiliario_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """

        if agente_imobiliario_id:
            return f"{cls.endpoint}{agente_imobiliario_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_agentes(
        self, agente_logado, agente_imobiliario_factory
    ):
        """
        test_agente_super_user_delete_agentes

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        agente_imobiliario = agente_imobiliario_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_agentes(self, agente_logado, agente_imobiliario_factory):
        """
        test_agente_delete_agentes

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        agente_imobiliario = agente_imobiliario_factory()
        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_proprietario_delete_agentes(
        self, proprietario_logado, agente_imobiliario_factory
    ):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        agente_imobiliario = agente_imobiliario_factory()

        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_agentes(
        self, inquilino_logado, agente_imobiliario_factory
    ):
        """
        test_inquilino_delete_agentes

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        agente_imobiliario = agente_imobiliario_factory()
        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_delete_agentes(self, api_client, agente_imobiliario_factory):
        """
        test_anonymous_delete_agentes

        Testa a exclusão de um agente por um usuario anonimo

        Args:
            api_client (dict): Retorna um client
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """

        agente_imobiliario = agente_imobiliario_factory()
        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
