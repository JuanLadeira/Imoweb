from http import HTTPStatus
from logging import getLogger

import pytest

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestListInquilinoEndpoint:
    """
    Agrupa os testes de listagem de inquilinos
    """

    endpoint = "/api/users/inquilinos/"

    def test_agente_super_user_list_inquilinos(self, agente_logado):
        """
        test_agente_super_user_list_inquilinos

        Testa a listagem de inquilinos por um super usuário

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

    def test_agente_list_inquilinos(self, agente_logado):
        """
        test_agente_list_inquilinos

        Testa a listagem de inquilinos por um agente

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

    def test_proprietario_list_inquilinos(self, proprietario_logado):
        """
        test_proprietario_list_inquilinos

        Testa a listagem de inquilinos por um proprietário


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

    def test_inquilino_list_inquilinos(self, inquilino_logado):
        """
        test_inquilino_list_inquilinos

        Testa a listagem de inquilinos por um inquilino

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
