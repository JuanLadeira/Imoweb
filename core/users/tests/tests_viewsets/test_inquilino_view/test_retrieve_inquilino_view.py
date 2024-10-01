from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestRetrieveInquilinoEndpoint:
    """
    Agrupa os testes de recuperação de inquilinos
    """

    endpoint = "/api/users/inquilinos/"

    @classmethod
    def get_endpoint(cls, inquilino_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            inquilino_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """
        if inquilino_id:
            return f"{cls.endpoint}{inquilino_id}/"
        return cls.endpoint

    def test_agente_super_user_retrieves_inquilinos(
        self, agente_logado, inquilino_factory
    ):
        """
        test_agente_super_user_retrieves_inquilinos

        Testa a recuperação de inquilinos por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilinos
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        inquilino = inquilino_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(inquilino.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_retrieves_inquilinos(self, agente_logado, inquilino_factory):
        """
        test_agente_retrieves_inquilinos

        Testa a recuperação de inquilinos por um agente

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilinos
        """
        dados = agente_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_retrieves_inquilinos(
        self, proprietario_logado, inquilino_factory
    ):
        """
        test_proprietario_retrieves_inquilinos

        Testa a recuperação de inquilinos por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilinos
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        inquilino = inquilino_factory()

        url = self.get_endpoint(inquilino.id)

        response = api_client.get(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code

    def test_inquilino_retrieves_inquilinos(self, inquilino_logado, inquilino_factory):
        """
        test_inquilino_retrieves_inquilinos

        Testa a recuperação de inquilinos por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            inquilino_factory (AgenteImobiliarioFactory): Factory de inquilinos
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        response = api_client.get(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NOT_FOUND, response.status_code
