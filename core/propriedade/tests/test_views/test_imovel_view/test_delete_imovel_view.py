from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestDeleteImovelEndpoint:
    endpoint = "/api/imoveis/"

    @classmethod
    def get_endpoint(cls, imovel_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            imovel_id (_type_, optional): recebe um tipo de imovel

        """
        if imovel_id:
            return f"{cls.endpoint}{imovel_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_imovel(self, agente_logado, imovel_factory):
        """
        test_agente_super_user_delete_imovel

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory): (ImovelFactory): Factory de imovel
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        imovel = imovel_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_imovel(self, agente_logado, imovel_factory):
        """
        test_agente_delete_imovel

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory): (AgenteImobiliarioFactory): Factory de imovel imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()
        url = self.get_endpoint(imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_imovel(self, proprietario_logado, imovel_factory):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            imovel_factory): (AgenteImobiliarioFactory): Factory de imovel imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()

        url = self.get_endpoint(imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_imovel(self, inquilino_logado, imovel_factory):
        """
        test_inquilino_delete_imovel

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            imovel_factory): (AgenteImobiliarioFactory): Factory de imovel imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()

        url = self.get_endpoint(imovel.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
