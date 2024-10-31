from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestdeleteCidadeEndpoint:
    endpoint = "/api/imoveis/cidades/"

    @classmethod
    def get_endpoint(cls, cidade_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            cidade_id (_type_, optional): recebe um id de um agente imobiliário. Defaults to None.

        """

        if cidade_id:
            return f"{cls.endpoint}{cidade_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_cidades(self, agente_logado, cidade_factory):
        """
        test_agente_super_user_delete_cidades

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (AgenteImobiliarioFactory): Factory de cidades imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        cidade = cidade_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(cidade.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_cidades(self, agente_logado, cidade_factory):
        """
        test_agente_delete_cidades

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            cidade_factory (AgenteImobiliarioFactory): Factory de cidades imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        cidade = cidade_factory()
        url = self.get_endpoint(cidade.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_cidades(self, proprietario_logado, cidade_factory):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            cidade_factory (AgenteImobiliarioFactory): Factory de cidades imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        cidade = cidade_factory()

        url = self.get_endpoint(cidade.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_cidades(self, inquilino_logado, cidade_factory):
        """
        test_inquilino_delete_cidades

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            cidade_factory (AgenteImobiliarioFactory): Factory de cidades imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        cidade = cidade_factory()
        url = self.get_endpoint(cidade.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
