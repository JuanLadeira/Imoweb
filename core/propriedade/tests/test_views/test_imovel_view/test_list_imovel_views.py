from http import HTTPStatus
from logging import getLogger

import pytest

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestListImovelEndpoint:
    """
    Agrupa os testes de listagem de imoveis
    """

    endpoint = "/api/imoveis/"

    def test_agente_super_user_list_imoveis(self, agente_logado):
        """
        test_agente_super_user_list_imoveis

        Testa a listagem de imoveis por um super usuário

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

    def test_agente_list_imoveis(self, agente_logado):
        """
        test_agente_list_imoveis

        Testa a listagem de imoveis por um agente

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

    def test_proprietario_list_imoveis(self, proprietario_logado):
        """
        test_proprietario_list_imoveis

        Testa a listagem de imoveis por um proprietário


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

    def test_imovel_list_imoveis(self, inquilino_logado):
        """
        test_imovel_list_imoveis

        Testa a listagem de imoveis por um imovel

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do imovel logado
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_anonymous_user_list_imoveis(self, api_client):
        """
        test_anonymous_user_list_imoveis

        Testa a listagem de imoveis por um usuário anônimo

        Args:
            api_client (APIClient): Instância do APIClient sem autenticação
        """
        response = api_client.get(
            self.endpoint,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code
