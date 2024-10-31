from http import HTTPStatus
from logging import getLogger

import pytest
from django.forms import model_to_dict

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdateImovelEndpoint:
    endpoint = "/api/imoveis/"

    @classmethod
    def get_endpoint(cls, imovel_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            imovel (_type_, optional): recebe um id de um imovel. Defaults to None.

        """

        if imovel_id:
            return f"{cls.endpoint}{imovel_id}/"
        return cls.endpoint

    def test_agente_super_user_update_imovel(self, agente_logado, imovel_factory):
        """
        test_agente_super_user_update_imovel

        Testa a atualização de imovel por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            (imovel_factory): Factory de imovel
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        imovel = imovel_factory()
        imovel_update = imovel_factory.build()
        imovel_data = model_to_dict(imovel_update)

        api_client = dados["api_client"]

        url = self.get_endpoint(imovel.id)

        data = {
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_imovel(self, agente_logado, imovel_factory):
        """
        test_agente_update_imovel

        Testa a atualização de imovel por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            (imovel_factory): Factory de imovel
        """
        dados = agente_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()
        imovel_update = imovel_factory.build()
        imovel_data = model_to_dict(imovel_update)
        url = self.get_endpoint(imovel.id)

        data = {
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_imovel(self, proprietario_logado, imovel_factory):
        """
        Testa a atualização de imovel por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            (imovel_factory): Factory de imovel
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        imovel = imovel_factory()
        imovel_update = imovel_factory.build()
        imovel_data = model_to_dict(imovel_update)

        url = self.get_endpoint(imovel.id)

        data = {
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_inquilino_update_imovel(
        self,
        inquilino_logado,
        imovel_factory,
    ):
        """
        test_inquilino_update_imovel

        Testa a atualização de imovel por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            (imovel_factory): Factory de imovel
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()
        imovel_update = imovel_factory.build()
        imovel_data = model_to_dict(imovel_update)
        url = self.get_endpoint(imovel.id)

        data = {
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_usuario_anonimo_update_imovel(self, api_client, imovel_factory):
        """
        test_usuario_anonimo_update_imovel

        Testa a atualização de imovel por um usuário anônimo

        Args:
            api_client (APIClient): Cliente API não autenticado
            (imovel_factory): Factory de imovel
        """
        imovel = imovel_factory()
        imovel_update = imovel_factory.build()
        imovel_data = model_to_dict(imovel_update)
        url = self.get_endpoint(imovel.id)

        data = {
            "preco": imovel_data.get("preco"),
            "preco_locacao": imovel_data.get("preco_locacao"),
            "area": imovel_data.get("area"),
            "quartos": imovel_data.get("quartos"),
            "banheiros": imovel_data.get("banheiros"),
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.UNAUTHORIZED, response.status_code
