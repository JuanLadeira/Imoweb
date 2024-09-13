from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestdeleteInquilinoEndpoint:
    endpoint = "/api/users/inquilinos/"

    @classmethod
    def get_endpoint(cls, inquilino_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            inquilino_id (_type_, optional): recebe um id de um inquilino imobiliário. Defaults to None.

        """

        if inquilino_id:
            return f"{cls.endpoint}{inquilino_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_inquilinos(
        self, agente_logado, inquilino_factory
    ):
        """
        test_agente_super_user_delete_inquilinos

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            inquilino_factory (inquilinoImobiliarioFactory): Factory de inquilinos imobiliários
        """
        dados = agente_logado
        inquilino = dados["agente"]
        inquilino.user.is_superuser = True
        inquilino.user.save()

        inquilino = inquilino_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(inquilino.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_inquilinos(self, agente_logado, inquilino_factory):
        """
        test_inquilino_delete_inquilinos

        Testa a exclusão de um inquilino por um inquilino

        Args:

            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            inquilino_factory (inquilinoImobiliarioFactory): Factory de inquilinos imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_inquilinos(
        self, proprietario_logado, inquilino_factory
    ):
        """
        Testa a exclusão de um inquilino por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            inquilino_factory (inquilinoImobiliarioFactory): Factory de inquilinos imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        inquilino = inquilino_factory()

        url = self.get_endpoint(inquilino.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_inquilinos(self, inquilino_logado, inquilino_factory):
        """
        test_inquilino_delete_inquilinos

        Testa a exclusão de um inquilino por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            inquilino_factory (inquilinoImobiliarioFactory): Factory de inquilinos imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        inquilino = inquilino_factory()
        url = self.get_endpoint(inquilino.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
