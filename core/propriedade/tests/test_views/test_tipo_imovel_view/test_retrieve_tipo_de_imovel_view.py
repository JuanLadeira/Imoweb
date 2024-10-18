from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestRetrieveTipoDeImovelEndpoint:
    """
    Agrupa os testes de recuperação de tipo_de_imoveis
    """

    endpoint = "/api/imoveis/tipos-de-imoveis/"

    @classmethod
    def get_endpoint(cls, tipo_de_imoveis_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            tipo_de_imoveis_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """
        if tipo_de_imoveis_id:
            return f"{cls.endpoint}{tipo_de_imoveis_id}/"
        return cls.endpoint

    def test_agente_super_user_retrieves_tipo_de_imoveis(
        self, agente_logado, tipo_de_imovel_factory
    ):
        """
        test_agente_super_user_retrieves_tipo_de_imoveis

        Testa a recuperação de tipo_de_imoveis por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (TipoDeImovelFactory): Factory de tipo_de_imoveis
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        tipo_de_imovel = tipo_de_imovel_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_retrieves_tipo_de_imoveis(
        self, agente_logado, tipo_de_imovel_factory
    ):
        """
        test_agente_retrieves_tipo_de_imoveis

        Testa a recuperação de tipo_de_imoveis por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            tipo_de_imovel_factory (TipoDeImovelFactory): Factory de tipo_de_imoveis
        """
        dados = agente_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_retrieves_tipo_de_imoveis(
        self, proprietario_logado, tipo_de_imovel_factory
    ):
        """
        test_proprietario_retrieves_tipo_de_imoveis

        Testa a recuperação de tipo_de_imoveis por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            tipo_de_imovel_factory (TipoDeImovelFactory): Factory de tipo_de_imoveis
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        tipo_de_imovel = tipo_de_imovel_factory()

        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_inquilino_retrieves_tipo_de_imoveis(
        self, inquilino_logado, tipo_de_imovel_factory
    ):
        """
        test_inquilino_retrieves_tipo_de_imoveis

        Testa a recuperação de tipo_de_imoveis por um inquilino logado

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            tipo_de_imovel_factory (TipoDeImovelFactory): Factory de tipo_de_imoveis
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        tipo_de_imovel = tipo_de_imovel_factory()
        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_anonymous_retrieves_tipo_de_imoveis(
        self, api_client, tipo_de_imovel_factory
    ):
        """
        test_anonymous_retrieves_tipo_de_imoveis

        Testa a recuperação de tipo_de_imoveis por um usuario anonimo

        Args:
            api_client (APIClient): Cliente da API
            tipo_de_imovel_factory (TipoDeImovelFactory): Factory de tipo_de_imoveis
        """

        tipo_de_imovel = tipo_de_imovel_factory()
        url = self.get_endpoint(tipo_de_imovel.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code
