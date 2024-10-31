from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateCidadeEndpoint:
    """
    Agrupa os testes de criação de Cidades
    """

    endpoint = "/api/imoveis/cidades/"

    def test_agente_super_create_cidade(
        self, agente_logado, cidade_factory, estado_factory
    ):
        """
        test_Cidade_super_cidade_create_Cidade

        Testa a criação de uma Cidade por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (cidadeFactory): Factory de cidades
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]
        estado = estado_factory()
        cidade = cidade_factory.build()

        cidade_data = model_to_dict(cidade)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_cidade(self, agente_logado, cidade_factory, estado_factory):
        """
        test_Cidade_create_cidade

        Testa a criação de um Cidade por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (CidadeFactory): Factory de cidades
        """
        dados = agente_logado
        api_client = dados["api_client"]

        estado = estado_factory()
        cidade = cidade_factory.build()

        cidade_data = model_to_dict(cidade)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_cidade(
        self, proprietario_logado, cidade_factory, estado_factory
    ):
        """
        test_proprietario_create_cidade

        Testa a criação de uma cidade por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            cidade_factory (_type_): _description_
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        cidade = cidade_factory.build()
        estado = estado_factory()

        cidade_data = model_to_dict(cidade)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }
        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_create_cidade(
        self, inquilino_logado, cidade_factory, estado_factory
    ):
        """
        test_inquilino_create_cidade

        testa a criação de uma cidade por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            cidade_factory (cidadeFactory): Factory de cidades
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        cidade = cidade_factory.build()
        estado = estado_factory()

        cidade_data = model_to_dict(cidade)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_create_cidade(self, api_client, cidade_factory, estado_factory):
        """
        test_inquilino_create_cidade

        testa a criação de uma cidade por um inquilino

        Args:
            api_client (_type_): Retorna um client
            cidade_factory (cidadeFactory): Factory de cidades
        """
        cidade = cidade_factory.build()
        estado = estado_factory()

        cidade_data = model_to_dict(cidade)

        data = {
            "nome": cidade_data.get("nome"),
            "estado": estado.id,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
