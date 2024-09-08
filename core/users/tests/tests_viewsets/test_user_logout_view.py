from http import HTTPStatus

import pytest

pytestmark = pytest.mark.django_db


class TestUserLogoutEndpoint:
    endpoint = "/api/auth/logout/"

    def test_agente_logout(self, agente_logado):
        dados = agente_logado
        api_client = dados["api_client"]
        refresh_token = dados["refresh"]
        response = api_client

        response = api_client.post(
            self.endpoint,
            data={
                "refresh_token": refresh_token,
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.RESET_CONTENT, response.data

    def test_proprietario_logout(self, proprietario_logado):
        dados = proprietario_logado
        api_client = dados["api_client"]
        refresh_token = dados["refresh"]
        response = api_client

        response = api_client.post(
            self.endpoint,
            data={
                "refresh_token": refresh_token,
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.RESET_CONTENT, response.data

    def test_inquilino_logout(self, inquilino_logado):
        dados = inquilino_logado
        api_client = dados["api_client"]
        refresh_token = dados["refresh"]
        response = api_client
        assert refresh_token is not None
        response = api_client.post(
            self.endpoint,
            data={"refresh_token": refresh_token},
            format="json",
        )
        assert response.status_code == HTTPStatus.RESET_CONTENT, response.data
