from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestdeleteProprietarioEndpoint:
    endpoint = "/api/users/proprietarios/"

    @classmethod
    def get_endpoint(cls, proprietario_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            proprietario_id (_type_, optional): recebe um id de um proprietario imobiliário. Defaults to None.

        """

        if proprietario_id:
            return f"{cls.endpoint}{proprietario_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_proprietarios(
        self, agente_logado, proprietario_factory
    ):
        """
        test_agente_super_user_delete_proprietarios

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            proprietario_factory (proprietarioImobiliarioFactory): Factory de proprietarios imobiliários
        """
        dados = agente_logado
        proprietario = dados["agente"]
        proprietario.user.is_superuser = True
        proprietario.user.save()

        proprietario = proprietario_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(proprietario.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_proprietarios(self, agente_logado, proprietario_factory):
        """
        test_proprietario_delete_proprietarios

        Testa a exclusão de um proprietario por um proprietario

        Args:

            proprietario_logado (dict): Retorna um dict com os dados do proprietario logado
            proprietario_factory (proprietarioImobiliarioFactory): Factory de proprietarios imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_proprietarios(
        self, proprietario_logado, proprietario_factory
    ):
        """
        Testa a exclusão de um proprietario por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            proprietario_factory (proprietarioImobiliarioFactory): Factory de proprietarios imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        proprietario = proprietario_factory()

        url = self.get_endpoint(proprietario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_proprietarios(
        self, inquilino_logado, proprietario_factory
    ):
        """
        test_proprietario_delete_proprietarios

        Testa a exclusão de um proprietario por um proprietario

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietario logado
            proprietario_factory (proprietarioImobiliarioFactory): Factory de proprietarios imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_delete_proprietarios(self, api_client, proprietario_factory):
        """
        test_anonymous_delete_proprietarios

        Testa a exclusão de um proprietario por um proprietario

        Args:
            api_client (APIClient): Cliente da API
            proprietario_factory (proprietarioImobiliarioFactory): Factory de proprietarios imobiliários
        """
        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
