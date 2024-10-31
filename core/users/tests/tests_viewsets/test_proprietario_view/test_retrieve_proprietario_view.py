from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestRetrieveProprietarioEndpoint:
    """
    Agrupa os testes de recuperação de proprietarios
    """

    endpoint = "/api/users/proprietarios/"

    @classmethod
    def get_endpoint(cls, proprietario_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            proprietario_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """
        if proprietario_id:
            return f"{cls.endpoint}{proprietario_id}/"
        return cls.endpoint

    def test_agente_super_user_retrieves_proprietarios(
        self, agente_logado, proprietario_factory
    ):
        """
        test_agente_super_user_retrieves_proprietarios

        Testa a recuperação de proprietarios por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietarios
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        proprietario = proprietario_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(proprietario.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_retrieves_proprietarios(self, agente_logado, proprietario_factory):
        """
        test_agente_retrieves_proprietarios

        Testa a recuperação de proprietarios por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietarios
        """
        dados = agente_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_retrieves_proprietarios(
        self, proprietario_logado, proprietario_factory
    ):
        """
        test_proprietario_retrieves_proprietarios

        Testa a recuperação de proprietarios por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietarios
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        proprietario = proprietario_factory()

        url = self.get_endpoint(proprietario.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code

        user = dados["proprietario"]
        url = self.get_endpoint(user.id)
        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code
        assert response.data["id"] == user.id

    def test_inquilino_retrieves_proprietarios(
        self, inquilino_logado, proprietario_factory
    ):
        """
        test_proprietario_retrieves_proprietarios

        Testa a recuperação de proprietarios por um proprietario

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietario logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietarios
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code

    def test_anonymous_retrieves_proprietarios(self, api_client, proprietario_factory):
        """
        test_anonymous_retrieves_proprietarios

        Testa a recuperação de proprietarios por um usuario anonimo

        Args:
            api_client (APIClient): Cliente de API
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietarios
        """
        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
