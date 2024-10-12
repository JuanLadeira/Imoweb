import io
from http import HTTPStatus
from logging import getLogger

import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from PIL import Image

pytestmark = pytest.mark.django_db


log = getLogger(__name__)


class TestCreateFotoEndpoint:
    """
    Agrupa os testes de criação de Fotos
    """

    endpoint = "/api/propriedades/fotos/"

    @classmethod
    def create_test_image_file(cls):
        image = Image.new("RGB", (100, 100), color="red")
        image_io = io.BytesIO()
        image.save(image_io, format="JPEG")
        image_io.seek(0)

        return SimpleUploadedFile(
            name="test_image.jpg",
            content=image_io.read(),
            content_type="image/jpeg",
        )

    def test_agente_super_create_foto(self, agente_logado, imovel_factory):
        """
        test_Foto_super_Foto_create_Foto

        Testa a criação de uma Foto por um super usuário

        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (ImovelFactory): Factory de Fotos
        """
        dados = agente_logado
        agente = dados["agente"]
        agente.user.is_superuser = True
        agente.user.save()

        api_client = dados["api_client"]
        imovel = imovel_factory()

        image_file = self.create_test_image_file()

        data = {
            "imovel": imovel.id,
            "foto": image_file,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="multipart",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_agente_create_foto(self, agente_logado, imovel_factory):
        """
        test_Foto_create_Foto

        Testa a criação de um Foto por um agente


        Args:
            agente_logado (dict): Retorna um dict com os dados do agente logado
            imovel_factory (ImovelFactory): Factory de Fotos
        """
        dados = agente_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()

        image_file = self.create_test_image_file()

        data = {
            "imovel": imovel.id,
            "foto": image_file,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="multipart",
        )
        log.info(response)
        assert response.status_code == HTTPStatus.CREATED, response.status_code

    def test_proprietario_create_foto(self, proprietario_logado, imovel_factory):
        """
        test_proprietario_create_Foto

        Testa a criação de uma Foto por um proprietário

        Args:
            proprietario_logado (dict): Retorna um dict com os dados do proprietário logado
            imovel_factory (_type_): _description_
        """
        dados = proprietario_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()

        image_file = self.create_test_image_file()

        data = {
            "imovel": imovel.id,
            "foto": image_file,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="multipart",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code

    def test_inquilino_create_foto(self, inquilino_logado, imovel_factory):
        """
        test_inquilino_create_Foto

        testa a criação de uma Foto por um inquilino

        Args:
            inquilino_logado (dict): Retorna um dict com os dados do inquilino logado
            imovel_factory (ImovelFactory): Factory de Fotos
        """
        dados = inquilino_logado
        api_client = dados["api_client"]

        imovel = imovel_factory()

        image_file = self.create_test_image_file()

        data = {
            "imovel": imovel.id,
            "foto": image_file,
        }

        response = api_client.post(
            self.endpoint,
            data=data,
            format="multipart",
        )

        assert response.status_code == HTTPStatus.FORBIDDEN, response.status_code
