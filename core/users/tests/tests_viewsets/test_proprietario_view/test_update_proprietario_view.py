from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateProprietarioEndpoint:
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

    def test_agente_super_user_update_proprietario(
        self, agente_logado, proprietario_factory
    ):
        """
        test_agente_super_user_update_proprietario

        Testa a atualização de proprietario por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietario imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        proprietario = proprietario_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(proprietario.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_proprietario(self, agente_logado, proprietario_factory):
        """
        test_agente_update_proprietario

        Testa a atualização de proprietario por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietario imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_proprietario(
        self, proprietario_logado, proprietario_factory
    ):
        """
        Testa a atualização de proprietario por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietario imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        proprietario = proprietario_factory()

        url = self.get_endpoint(proprietario.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_proprietario(
        self, inquilino_logado, proprietario_factory
    ):
        """
        test_inquilino_update_proprietario

        Testa a atualização de proprietario por um proprietario

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietario logado
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietario imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_update_proprietario(self, api_client, proprietario_factory):
        """
        test_anonymous_update_proprietario

        Testa a atualização de proprietario por um usuario anonimo

        Args:
            api_client (APIClient): Cliente da API
            proprietario_factory (AgenteImobiliarioFactory): Factory de proprietario imobiliários
        """
        proprietario = proprietario_factory()
        url = self.get_endpoint(proprietario.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
