from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateAgenteEndpoint:
    endpoint = "/api/users/agentes/"

    def test_agente_super_user_create_agente(self, agente_logado, user_factory):
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]

        user = user_factory.build()

        user_data = model_to_dict(user)

        data = {
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.data

    def test_agente_create_agente(self, agente_logado, user_factory):
        dados = agente_logado
        api_client = dados["api_client"]

        user = user_factory.build()

        user_data = model_to_dict(user)

        data = {
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.FORBIDDEN, response.data

    def test_proprietario_create_agente(self, proprietario_logado, user_factory):
        dados = proprietario_logado
        api_client = dados["api_client"]
        refresh_token = dados["refresh"]

        user = user_factory.build()

        user_data = model_to_dict(user)

        data = {
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        response = api_client.post(
            self.endpoint,
            data={
                "refresh_token": refresh_token,
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.data

    def test_inquilino_create_agente(self, inquilino_logado, user_factory):
        dados = inquilino_logado
        api_client = dados["api_client"]

        user = user_factory.build()

        user_data = model_to_dict(user)

        data = {
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        response = api_client.post(
            self.endpoint,
            data={},
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
