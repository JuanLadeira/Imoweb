from http import HTTPStatus
from logging import getLogger

import pytest

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestListProprietarioEndpoint:
    """
    Agrupa os testes de listagem de proprietarios
    """

    endpoint = "/api/users/proprietarios/"

    def test_agente_super_user_list_proprietarios(self, agente_logado):
        """
        test_agente_super_user_list_proprietarios

        Testa a listagem de proprietarios por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.data

    def test_agente_list_proprietarios(self, agente_logado):
        """
        test_agente_list_proprietarios

        Testa a listagem de proprietarios por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
        """
        dados = agente_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.OK, response.data

    def test_proprietario_list_proprietarios(self, proprietario_logado):
        """
        test_proprietario_list_proprietarios

        Testa a listagem de proprietarios por um proprietário


        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

        assert len(response.data) == 1, len(response.data)

    def test_inquilino_list_proprietarios(self, inquilino_logado):
        """
        test_inquilino_list_proprietarios

        Testa a listagem de proprietarios por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code
        assert len(response.data) == 0, len(response.data)

    def test_anonymous_list_proprietarios(self, api_client):
        """
        test_anonymous_list_proprietarios

        Testa a listagem de proprietarios por um inquilino

        Args:
            api_client (APIClient): Cliente para realizar requisições a API
        """

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
