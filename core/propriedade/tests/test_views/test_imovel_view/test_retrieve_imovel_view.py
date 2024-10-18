from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestImoveisEndpoint:
    """
    Agrupa os testes de recuperação de imoveis
    """

    endpoint = "/api/imoveis/"

    @classmethod
    def get_endpoint(cls, imovel_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            imovel_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """
        if imovel_id:
            return f"{cls.endpoint}{imovel_id}/"
        return cls.endpoint

    def test_agente_super_user_retrieves_imoveis(self, agente_logado, imovel_factory):
        """
        test_agente_super_user_retrieves_imoveis

        Testa a recuperação de imoveis por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (ImovelFactory): Factory de imoveis
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        imovel = imovel_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_retrieves_imoveis(self, agente_logado, imovel_factory):
        """
        test_agente_retrieves_imoveis

        Testa a recuperação de imoveis por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (AgenteImobiliarioFactory): Factory de imoveis
        """
        dados = agente_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()
        url = self.get_endpoint(imovel.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_retrieves_imoveis(self, proprietario_logado, imovel_factory):
        """
        test_proprietario_retrieves_imoveis

        Testa a recuperação de imoveis por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            imovel_factory (AgenteImobiliarioFactory): Factory de imoveis
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        imovel = imovel_factory()

        url = self.get_endpoint(imovel.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_inquilino_retrieves_imoveis(self, inquilino_logado, imovel_factory):
        """
        test_inquilino_retrieves_imoveis

        Testa a recuperação de imovel por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            imovel_factory (AgenteImobiliarioFactory): Factory de imoveis
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()
        url = self.get_endpoint(imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_anonymous_retrieves_imoveis(self, api_client, imovel_factory):
        """
        test_anonymous_retrieves_imoveis

        Testa a recuperação de imoveis por um usuario anonimo

        Args:
            api_client (APIClient): Cliente da API
            imovel_factory (AgenteImobiliarioFactory): Factory de imoveis
        """

        imovel = imovel_factory()
        url = self.get_endpoint(imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code
