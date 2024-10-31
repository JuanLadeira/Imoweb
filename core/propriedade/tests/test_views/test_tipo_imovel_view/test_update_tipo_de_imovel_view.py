from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateTipoDeImovelEndpoint:
    endpoint = "/api/imoveis/tipos-de-imoveis/"

    @classmethod
    def get_endpoint(cls, tipo_de_imovel=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            tipo_de_imovel (_type_, optional): recebe um id de um tipo_de_imovel. Defaults to None.

        """

        if tipo_de_imovel:
            return f"{cls.endpoint}{tipo_de_imovel}/"
        return cls.endpoint

    def test_agente_super_user_update_tipo_de_imovel(
        self, agente_logado, tipo_de_imovel_factory
    ):
        """
        test_agente_super_user_update_tipo_de_imovel

        Testa a atualização de tipo_de_imovel por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            (tipo_de_imovel_factory): Factory de tipo_de_imovel
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        tipo_de_imovel = tipo_de_imovel_factory()
        tipo_de_imovel_update = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel_update)

        api_client = dados["api_client"]

        url = self.get_endpoint(tipo_de_imovel.id)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_tipo_de_imovel(self, agente_logado, tipo_de_imovel_factory):
        """
        test_agente_update_tipo_de_imovel

        Testa a atualização de tipo_de_imovel por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            (tipo_de_imovel_factory): Factory de tipo_de_imovel
        """
        dados = agente_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        tipo_de_imovel_update = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel_update)
        url = self.get_endpoint(tipo_de_imovel.id)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_tipo_de_imovel(
        self, proprietario_logado, tipo_de_imovel_factory
    ):
        """
        Testa a atualização de tipo_de_imovel por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            (tipo_de_imovel_factory): Factory de tipo_de_imovel
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        tipo_de_imovel = tipo_de_imovel_factory()
        tipo_de_imovel_update = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel_update)

        url = self.get_endpoint(tipo_de_imovel.id)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_tipo_de_imovel(
        self,
        inquilino_logado,
        tipo_de_imovel_factory,
    ):
        """
        test_inquilino_update_tipo_de_imovel

        Testa a atualização de tipo_de_imovel por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            (tipo_de_imovel_factory): Factory de tipo_de_imovel
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        tipo_de_imovel_update = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel_update)
        url = self.get_endpoint(tipo_de_imovel.id)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_usuario_anonimo_update_tipo_de_imovel(
        self, api_client, tipo_de_imovel_factory
    ):
        """
        test_usuario_anonimo_update_tipo_de_imovel

        Testa a atualização de tipo_de_imovel por um usuário anônimo

        Args:
            api_client (APIClient): Cliente API não autenticado
            (tipo_de_imovel_factory): Factory de tipo_de_imovel
        """
        tipo_de_imovel = tipo_de_imovel_factory()
        tipo_de_imovel_update = tipo_de_imovel_factory.build()
        tipo_de_imovel_data = model_to_dict(tipo_de_imovel_update)
        url = self.get_endpoint(tipo_de_imovel.id)

        data = {
            "nome": tipo_de_imovel_data.get("nome"),
            "tipo": tipo_de_imovel_data.get("tipo"),
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
