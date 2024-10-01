from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateInquilinoEndpoint:
    """
    Agrupa os testes de criação de inquilinos
    """

    endpoint = "/api/users/inquilinos/"

    def test_agente_super_user_create_inquilino(self, agente_logado, user_factory):
        """
        test_agente_super_user_create_inquilino

        Testa a criação de um inquilino por um super usuário agente

        Args:a
            agente_logado (dict): Retorna um dict com os dados do agente logado
            user_factory (UserFactory): Factory de usuários
        """
        dados = agente_logado
        inquilino = dados["agente"]
        inquilino.user.is_superuser = True
        inquilino.user.save()

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
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_inquilino(self, agente_logado, user_factory):
        """
        test_agente_create_inquilino

        Testa a criação de um inquilino por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            user_factory (UserFactory): Factory de usuários
        """
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
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_inquilino(self, proprietario_logado, user_factory):
        """
        test_proprietario_create_inquilino

        Testa a criação de um inquilino por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            user_factory (_type_): _description_
        """
        dados = proprietario_logado
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

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_create_inquilino(self, inquilino_logado, user_factory):
        """
        test_inquilino_create_inquilino

        testa a criação de um inquilino por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            user_factory (UserFactory): Factory de usuários
        """
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

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
