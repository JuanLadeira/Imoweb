from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateAgenteEndpoint:
    """
    Agrupa os testes de criação de agentes
    """

    endpoint = "/api/users/agentes/"

    def test_agente_super_user_create_agente(self, agente_logado, user_factory):
        """
        test_agente_super_user_create_agente

        Testa a criação de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            user_factory (UserFactory): Factory de usuários
        """
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
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_agente(self, agente_logado, user_factory):
        """
        test_agente_create_agente

        Testa a criação de um agente por um agente


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
        log.info(response)
        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_proprietario_create_agente(self, proprietario_logado, user_factory):
        """
        test_proprietario_create_agente

        Testa a criação de um agente por um proprietário

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

    def test_inquilino_create_agente(self, inquilino_logado, user_factory):
        """
        test_inquilino_create_agente

        testa a criação de um agente por um inquilino

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

    def test_anonymous_create_agente(self, api_client, user_factory):
        """
        test_anonymous_create_agente

        testa a criação de um agente por um usuario anonimo

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            user_factory (UserFactory): Factory de usuários
        """
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

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
