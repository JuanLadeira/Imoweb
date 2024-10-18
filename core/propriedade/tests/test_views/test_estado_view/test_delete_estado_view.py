from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestDeleteEstadoEndpoint:
    endpoint = "/api/imoveis/estados/"

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

    def test_agente_super_user_delete_estados(self, agente_logado, estado_factory):
        """
        test_agente_super_user_delete_estados

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            estado_factory (AgenteImobiliarioFactory): Factory de estados imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        estado = estado_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(estado.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_estados(self, agente_logado, estado_factory):
        """
        test_agente_delete_estados

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            estado_factory (AgenteImobiliarioFactory): Factory de estados imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        estado = estado_factory()
        url = self.get_endpoint(estado.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_estados(self, proprietario_logado, estado_factory):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            estado_factory (AgenteImobiliarioFactory): Factory de estados imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        estado = estado_factory()

        url = self.get_endpoint(estado.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_estados(self, inquilino_logado, estado_factory):
        """
        test_inquilino_delete_estados

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            estado_factory (AgenteImobiliarioFactory): Factory de estados imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        estado = estado_factory()
        url = self.get_endpoint(estado.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
