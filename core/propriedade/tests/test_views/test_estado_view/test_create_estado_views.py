from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateEstadoEndpoint:
    """
    Agrupa os testes de criação de estados
    """

    endpoint = "/api/propriedades/estados/"

    def test_agente_super_create_estado(self, agente_logado, estado_factory):
        """
        test_estado_super_estado_create_estado

        Testa a criação de uma estado por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            estado_factory (estadoFactory): Factory de estados
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]
        estado = estado_factory.build()

        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_estado(self, agente_logado, estado_factory):
        """
        test_estado_create_estado

        Testa a criação de um estado por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            estado_factory (estadoFactory): Factory de estados
        """
        dados = agente_logado
        api_client = dados["api_client"]

        estado = estado_factory.build()

        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_estado(self, proprietario_logado, estado_factory):
        """
        test_proprietario_create_estado

        Testa a criação de uma estado por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            estado_factory (_type_): _description_
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        estado = estado_factory.build()

        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_create_estado(self, inquilino_logado, estado_factory):
        """
        test_inquilino_create_estado

        testa a criação de uma estado por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            estado_factory (estadoFactory): Factory de estados
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        estado = estado_factory.build()

        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_create_estado(self, api_client, estado_factory):
        """
        test_inquilino_create_estado

        testa a criação de uma estado por um inquilino

        Args:
            api_client (_type_): Retorna um client
            estado_factory (estadoFactory): Factory de estados
        """
        estado = estado_factory.build()

        estado_data = model_to_dict(estado)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
