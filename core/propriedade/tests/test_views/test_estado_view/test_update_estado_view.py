from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateEstadoEndpoint:
    endpoint = "/api/propriedades/estados/"

    @classmethod
    def get_endpoint(cls, estado_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            estado_id (_type_, optional): recebe um id de um estado. Defaults to None.

        """

        if estado_id:
            return f"{cls.endpoint}{estado_id}/"
        return cls.endpoint

    def test_agente_super_user_update_estados(self, agente_logado, estado_factory):
        """
        test_agente_super_user_update_estados

        Testa a atualização de estados por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            (estado_factory): Factory de estados
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        estado = estado_factory()
        estado_update = estado_factory.build()
        estado_data = model_to_dict(estado_update)
        estado = estado_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(estado.id)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_estados(self, agente_logado, estado_factory):
        """
        test_agente_update_estados

        Testa a atualização de estados por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            (estado_factory): Factory de estados
        """
        dados = agente_logado
        api_client = dados["api_client"]

        estado = estado_factory()
        estado_update = estado_factory.build()
        estado_data = model_to_dict(estado_update)
        estado = estado_factory()
        url = self.get_endpoint(estado.id)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_estados(self, proprietario_logado, estado_factory):
        """
        Testa a atualização de estados por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            (estado_factory): Factory de estados
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        estado = estado_factory()
        estado_update = estado_factory.build()
        estado_data = model_to_dict(estado_update)
        estado = estado_factory()

        url = self.get_endpoint(estado.id)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_estados(
        self,
        inquilino_logado,
        estado_factory,
    ):
        """
        test_inquilino_update_estados

        Testa a atualização de estados por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            (estado_factory): Factory de estados
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        estado = estado_factory()
        estado_update = estado_factory.build()
        estado_data = model_to_dict(estado_update)
        estado = estado_factory()
        url = self.get_endpoint(estado.id)

        data = {
            "nome": estado_data.get("nome"),
            "uf": estado_data.get("uf"),
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
