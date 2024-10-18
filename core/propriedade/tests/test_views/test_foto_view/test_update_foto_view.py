from http import HTTPStatus
from logging import getLogger

import pytest

log = getLogger(__name__)


@pytest.mark.django_db()
class TestUpdatefotoEndpoint:
    endpoint = "/api/imoveis/fotos/"

    @classmethod
    def get_endpoint(cls, foto_id=None):
        """
        get_endpoint

        Retorna a url do endpoint

        Args:
            foto (_type_, optional): recebe um id de um foto. Defaults to None.

        """

        if foto_id:
            return f"{cls.endpoint}{foto_id}/"
        return cls.endpoint

    def test_agente_super_user_update_fotos(
        self, agente_logado, foto_factory, imovel_factory
    ):
        """
        test_agente_super_user_update_fotos

        Testa a atualização de fotos por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            (foto_factory): Factory de fotos
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        foto = foto_factory()
        imovel = imovel_factory()

        api_client = dados["api_client"]

        url = self.get_endpoint(foto.id)

        data = {
            "imovel": imovel.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_agente_update_fotos(self, agente_logado, foto_factory, imovel_factory):
        """
        test_agente_update_fotos

        Testa a atualização de fotos por um agente

        Args:

            agente_logado (dict): Retorna um dict com os dados do agente logado
            (foto_factory): Factory de fotos
        """
        dados = agente_logado
        api_client = dados["api_client"]

        foto = foto_factory()
        imovel = imovel_factory()

        url = self.get_endpoint(foto.id)

        data = {
            "imovel": imovel.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_proprietario_update_fotos(
        self, proprietario_logado, foto_factory, imovel_factory
    ):
        """
        Testa a atualização de fotos por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            (foto_factory): Factory de fotos
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        foto = foto_factory()
        imovel = imovel_factory()

        url = self.get_endpoint(foto.id)

        data = {
            "imovel": imovel.id,
        }

        response = api_client.patch(
            url,
            data=data,
            format="json",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_update_fotos(
        self,
        inquilino_logado,
        foto_factory,
        imovel_factory,
    ):
        """
        test_inquilino_update_fotos

        Testa a atualização de fotos por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            (foto_factory): Factory de fotos
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        foto = foto_factory()
        imovel = imovel_factory()

        url = self.get_endpoint(foto.id)

        data = {
            "imovel": imovel.id,
        }

        response = api_client.patch(url, data=data, format="json")

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
