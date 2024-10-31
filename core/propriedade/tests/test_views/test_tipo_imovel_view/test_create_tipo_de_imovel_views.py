from http import HTTPStatus
from logging import getLogger

import pytest

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateTipoDeImoveisEndpoint:
    """
    Agrupa os testes de criação de tipodeimoveiss
    """

    endpoint = "/api/imoveis/tipos-de-imoveis/"

    def test_agente_super_create_tipodeimoveis(
        self, agente_logado, tipo_de_imovel_factory
    ):
        """
        test_tipodeimoveis_super_tipodeimoveis_create_tipodeimoveis

        Testa a criação de uma tipodeimoveis por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (tipo_de_imovel_factory): Factory de tipodeimoveiss
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]
        tipo_de_imovel = tipo_de_imovel_factory.build()

        data = {
            "nome": tipo_de_imovel.nome,
            "tipo": tipo_de_imovel.tipo,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_tipodeimoveis(self, agente_logado, tipo_de_imovel_factory):
        """
        test_tipodeimoveis_create_tipodeimoveis

        Testa a criação de um tipodeimoveis por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (tipo_de_imovel_factory): Factory de tipodeimoveiss
        """
        dados = agente_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory.build()

        data = {
            "nome": tipo_de_imovel.nome,
            "tipo": tipo_de_imovel.tipo,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_tipodeimoveis(
        self, proprietario_logado, tipo_de_imovel_factory
    ):
        """
        test_proprietario_create_tipodeimoveis

        Testa a criação de uma tipodeimoveis por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            tipo_de_imovel_factory (_type_): _description_
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory.build()

        data = {
            "nome": tipo_de_imovel.nome,
            "tipo": tipo_de_imovel.tipo,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_create_tipodeimoveis(
        self, inquilino_logado, tipo_de_imovel_factory
    ):
        """
        test_inquilino_create_tipodeimoveis

        testa a criação de uma tipodeimoveis por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            tipo_de_imovel_factory (tipo_de_imovel_factory): Factory de tipodeimoveiss
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory.build()

        data = {"nome": tipo_de_imovel.nome, "tipo": tipo_de_imovel.tipo}

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_create_tipodeimoveis(self, api_client, tipo_de_imovel_factory):
        """
        test_inquilino_create_tipodeimoveis

        testa a criação de uma tipodeimoveis por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            tipo_de_imovel_factory (tipo_de_imovel_factory): Factory de tipodeimoveiss
        """

        tipo_de_imovel = tipo_de_imovel_factory.build()

        data = {"nome": tipo_de_imovel.nome, "tipo": tipo_de_imovel.tipo}

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
