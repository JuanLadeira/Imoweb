# ruff: noqa: PLR0913
from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateImoveisEndpoint:
    """
    Agrupa os testes de criação de imoveis
    """

    endpoint = "/api/imoveis/"

    def test_agente_super_create_imoveis(
        self,
        agente_logado,
        imovel_factory,
        cidade_factory,
        proprietario_factory,
        tipo_de_imovel_factory,
    ):
        """
        test_imoveis_super_imoveis_create_imoveis

        Testa a criação de uma imoveis por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (imovel_factory): Factory de imoveis
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]

        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()

        imovel_data = model_to_dict(imovel)

        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_imoveis(
        self,
        agente_logado,
        imovel_factory,
        cidade_factory,
        proprietario_factory,
        tipo_de_imovel_factory,
    ):
        """
        test_imoveis_create_imoveis

        Testa a criação de um imoveis por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (imovel_factory): Factory de imoveis
        """
        dados = agente_logado
        api_client = dados["api_client"]

        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()

        imovel_data = model_to_dict(imovel)

        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_imoveis(
        self,
        proprietario_logado,
        imovel_factory,
        cidade_factory,
        tipo_de_imovel_factory,
        proprietario_factory,
    ):
        """
        test_proprietario_create_imoveis

        Testa a criação de uma imoveis por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            imovel_factory (_type_): _description_
        """
        dados = proprietario_logado

        api_client = dados["api_client"]

        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()

        imovel_data = model_to_dict(imovel)

        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_inquilino_create_imoveis(
        self,
        inquilino_logado,
        imovel_factory,
        cidade_factory,
        tipo_de_imovel_factory,
        proprietario_factory,
    ):
        """
        test_inquilino_create_imoveis

        testa a criação de uma imoveis por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            imovel_factory (imovel_factory): Factory de imoveis
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()

        imovel_data = model_to_dict(imovel)

        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_anonymous_create_imoveis(
        self,
        api_client,
        imovel_factory,
        cidade_factory,
        tipo_de_imovel_factory,
        proprietario_factory,
    ):
        """
        test_inquilino_create_imoveis

        testa a criação de uma imoveis por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            imovel_factory (imovel_factory): Factory de imoveis
        """

        imovel = imovel_factory.build()
        cidade = cidade_factory()
        proprietario = proprietario_factory()
        tipo_de_imovel = tipo_de_imovel_factory()

        imovel_data = model_to_dict(imovel)

        data = {
            "proprietario": proprietario.id,
            "criado_por": proprietario.user.id,
            "endereco": imovel_data.get("endereco"),
            "cidade": cidade.id,
            "pais": imovel_data.get("pais"),
            "cep": imovel_data.get("cep"),
            "titulo": imovel_data.get("titulo"),
            "descricao": imovel_data.get("descricao"),
            "tipo": tipo_de_imovel.id,
            "tipo_de_contrato": imovel_data.get("tipo_de_contrato"),
            "status": imovel_data.get("status"),
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
            "vagas": imovel_data.get("vagas"),
            "iptu": imovel_data.get("iptu"),
            "condominio": imovel_data.get("condominio"),
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
