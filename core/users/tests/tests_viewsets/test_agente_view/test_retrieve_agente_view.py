from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestRetrieveAgenteEndpoint:
    """
    Agrupa os testes de recuperação de agentes
    """

    endpoint = "/api/users/agentes/"

    @classmethod
    def get_endpoint(cls, agente_imobiliario_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            agente_imobiliario_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """
        if agente_imobiliario_id:
            return f"{cls.endpoint}{agente_imobiliario_id}/"
        return cls.endpoint

    def test_agente_super_user_retrieves_agentes(
        self, agente_logado, agente_imobiliario_factory
    ):
        """
        test_agente_super_user_retrieves_agentes

        Testa a recuperação de agentes por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        agente_imobiliario = agente_imobiliario_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_retrieves_agentes(self, agente_logado, agente_imobiliario_factory):
        """
        test_agente_retrieves_agentes

        Testa a recuperação de agentes por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        agente_imobiliario = agente_imobiliario_factory()
        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_retrieves_agentes(
        self, proprietario_logado, agente_imobiliario_factory
    ):
        """
        test_proprietario_retrieves_agentes

        Testa a recuperação de agentes por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        agente_imobiliario = agente_imobiliario_factory()

        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code

    def test_inquilino_retrieves_agentes(
        self, inquilino_logado, agente_imobiliario_factory
    ):
        """
        test_inquilino_retrieves_agentes

        Testa a recuperação de agentes por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            agente_imobiliario_factory (AgenteImobiliarioFactory): Factory de agentes imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        agente_imobiliario = agente_imobiliario_factory()
        url = self.get_endpoint(agente_imobiliario.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code
