from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateInquilinoEndpoint:
    endpoint = "/api/users/inquilinos/"

    @classmethod
    def get_endpoint(cls, inquilino_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            inquilino_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """

        if inquilino_id:
            return f"{cls.endpoint}{inquilino_id}/"
        return cls.endpoint

    def test_agente_super_user_update_inquilino(self, agente_logado, inquilino_factory):
        """
        test_agente_super_user_update_inquilino

        Testa a atualização de inquilino por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilino imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        inquilino = inquilino_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(inquilino.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_inquilino(self, agente_logado, inquilino_factory):
        """
        test_agente_update_inquilino

        Testa a atualização de inquilino por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilino imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_inquilino(
        self, proprietario_logado, inquilino_factory
    ):
        """
        Testa a atualização de inquilino por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilino imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        inquilino = inquilino_factory()

        url = self.get_endpoint(inquilino.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_inquilino(self, inquilino_logado, inquilino_factory):
        """
        test_inquilino_update_inquilino

        Testa a atualização de inquilino por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilino imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_update_inquilino(self, api_client, inquilino_factory):
        """
        test_anonymous_update_inquilino

        Testa a atualização de inquilino por um usuario anonimo

        Args:
            api_client (APIClient): Cliente da API
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilino imobiliários
        """
        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        data = {
            "first_name": "Teste",
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
