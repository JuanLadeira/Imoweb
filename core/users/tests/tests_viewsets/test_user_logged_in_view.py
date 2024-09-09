# ruff: noqa: S106

from http import HTTPStatus

import pytest

pytestmark = pytest.mark.django_db


class TestUserLoggedInEndpoint:
    endpoint = "/api/users/user_logged_in/"

    def test_agente_login(self, api_client, agente_imobiliario_factory, user_factory):
        user = user_factory(password="password", is_superuser=False)

        agente = agente_imobiliario_factory(
            user=user,
        )
        agente.save()
        response = api_client.post(
            "/api/auth/token/",
            {
                "username": agente.user.username,
                "password": "password",
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.OK
        token = response.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

        response = api_client.get(self.endpoint)
        assert response.status_code == HTTPStatus.OK

    def test_proprietario_login(self, api_client, proprietario_factory, user_factory):
        user = user_factory(password="password", is_superuser=False)

        proprietario = proprietario_factory(
            user=user,
        )
        proprietario.save()
        response = api_client.post(
            "/api/auth/token/",
            {
                "username": proprietario.user.username,
                "password": "password",
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.OK
        token = response.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

        response = api_client.get(self.endpoint)
        assert response.status_code == HTTPStatus.OK

    def test_inquilino_login(self, api_client, inquilino_factory, user_factory):
        user = user_factory(password="password", is_superuser=False)

        inquilino = inquilino_factory(
            user=user,
        )
        inquilino.save()
        response = api_client.post(
            "/api/auth/token/",
            {
                "username": inquilino.user.username,
                "password": "password",
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.OK
        token = response.data["access"]
        api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")

        response = api_client.get(self.endpoint)
        assert response.status_code == HTTPStatus.OK

    def test_inquilino_nao_ativo_login(
        self, api_client, inquilino_factory, user_factory
    ):
        user = user_factory(password="password", is_superuser=False, is_active=False)

        inquilino = inquilino_factory(
            user=user,
        )
        inquilino.save()
        response = api_client.post(
            "/api/auth/token/",
            {
                "username": inquilino.user.username,
                "password": "password",
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.UNAUTHORIZED
