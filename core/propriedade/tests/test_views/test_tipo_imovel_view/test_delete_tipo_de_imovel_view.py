from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestDeleteTipoDeImovelEndpoint:
    endpoint = "/api/imoveis/tipos-de-imoveis/"

    @classmethod
    def get_endpoint(cls, tipo_de_imovel_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            tipo_de_imovel_id (_type_, optional): recebe um tipo de imovel

        """

        if tipo_de_imovel_id:
            return f"{cls.endpoint}{tipo_de_imovel_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_tipo_de_imovel(
        self, agente_logado, tipo_de_imovel_factory
    ):
        """
        test_agente_super_user_delete_tipo_de_imovel

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (AgenteImobiliarioFactory): Factory de tipo_de_imovel
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        tipo_de_imovel = tipo_de_imovel_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_tipo_de_imovel(self, agente_logado, tipo_de_imovel_factory):
        """
        test_agente_delete_tipo_de_imovel

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (AgenteImobiliarioFactory): Factory de tipo_de_imovel imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_tipo_de_imovel(
        self, proprietario_logado, tipo_de_imovel_factory
    ):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            tipo_de_imovel_factory (AgenteImobiliarioFactory): Factory de tipo_de_imovel imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        tipo_de_imovel = tipo_de_imovel_factory()

        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_tipo_de_imovel(
        self, inquilino_logado, tipo_de_imovel_factory
    ):
        """
        test_inquilino_delete_tipo_de_imovel

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            tipo_de_imovel_factory (AgenteImobiliarioFactory): Factory de tipo_de_imovel imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
