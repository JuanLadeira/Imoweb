import logging
from http import HTTPStatus

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db

log = logging.getLogger(__name__)


class TestInquilinoCreateEndpoint:
    endpoint = "/api/users/inquilinos/"

    def test_agente_create_inquilino(
        self, agente_logado, inquilino_factory, user_factory
    ):
        dados = agente_logado
        api_client = dados["api_client"]

        user = user_factory.build()

        user_data = model_to_dict(user)

        inquilino_data = {
            "username": user_data["username"],
            "password": user_data["password"],
            "password2": user_data["password"],
        }

        response = api_client.post(
            self.endpoint,
            data=inquilino_data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.data

    def test_proprietario_create_inquilino(
        self, proprietario_logado, inquilino_factory
    ):
        dados = proprietario_logado
        api_client = dados["api_client"]
        refresh_token = dados["refresh"]

        inquilino = inquilino_factory.build()

        inquilino_data = model_to_dict(inquilino)

        log.info(inquilino_data)

        response = api_client.post(
            self.endpoint,
            data={
                "refresh_token": refresh_token,
            },
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.data

    def test_inquilino_create_inquilino(self, inquilino_logado, inquilino_factory):
        dados = inquilino_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory.build()

        inquilino_data = model_to_dict(inquilino)

        log.info(inquilino_data)

        response = api_client.post(
            self.endpoint,
            data={},
            format="json",
        )
        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
