from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestDeleteFotoEndpoint:
    endpoint = "/api/propriedades/fotos/"

    @classmethod
    def get_endpoint(cls, foto_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            foto_id (_type_, optional): recebe um id de um foto. Defaults to None.

        """

        if foto_id:
            return f"{cls.endpoint}{foto_id}/"
        return cls.endpoint

    def test_agente_super_user_delete_fotos(self, agente_logado, foto_factory):
        """
        test_agente_super_user_delete_fotos

        Testa a exclusão de um agente por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            foto_factory): (AgenteImobiliarioFactory): Factory de fotos imobiliários
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        foto = foto_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(foto.id)

        response = api_client.delete(
            url,
            format="json",
        )
        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_agente_delete_fotos(self, agente_logado, foto_factory):
        """
        test_agente_delete_fotos

        Testa a exclusão de um agente por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            foto_factory): (AgenteImobiliarioFactory): Factory de fotos imobiliários
        """
        dados = agente_logado
        api_client = dados["api_client"]

        foto = foto_factory()
        url = self.get_endpoint(foto.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.NO_CONTENT, response.status_code

    def test_proprietario_delete_fotos(self, proprietario_logado, foto_factory):
        """
        Testa a exclusão de um agente por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            foto_factory): (AgenteImobiliarioFactory): Factory de fotos imobiliários
        """
        dados = proprietario_logado
        api_client = dados["api_client"]
        foto = foto_factory()

        url = self.get_endpoint(foto.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_delete_fotos(self, inquilino_logado, foto_factory):
        """
        test_inquilino_delete_fotos

        Testa a exclusão de um agente por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            foto_factory): (AgenteImobiliarioFactory): Factory de fotos imobiliários
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        foto = foto_factory()
        url = self.get_endpoint(foto.id)

        response = api_client.delete(
            url,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
