from http import HTTPStatus
from logging import getLogger

import pytest

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestListAgenteEndpoint:
    """
    Agrupa os testes de listagem de agentes
    """

    endpoint = "/api/users/agentes/"

    def test_agente_super_user_list_agentes(self, agente_logado):
        """
        test_agente_super_user_list_agentes

        Testa a listagem de agentes por um super usuário

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

    def test_agente_list_agentes(self, agente_logado):
        """
        test_agente_list_agentes

        Testa a listagem de agentes por um agente

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

    def test_proprietario_list_agentes(self, proprietario_logado):
        """
        test_proprietario_list_agentes

        Testa a listagem de agentes por um proprietário


        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.data

    def test_inquilino_list_agentes(self, inquilino_logado):
        """
        test_inquilino_list_agentes

        Testa a listagem de agentes por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
