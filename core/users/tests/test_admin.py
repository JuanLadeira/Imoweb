from http import HTTPStatus

import pytest
from django.urls import reverse

from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario

pytestmark = pytest.mark.django_db


class TestAgenteAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_agenteimobiliario_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK

    def test_search(self, admin_client):
        url = reverse("admin:users_agenteimobiliario_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK

    def test_add(self, admin_client, agente_imobiliario_factory):
        url = reverse("admin:users_agenteimobiliario_add")
        response = admin_client.get(url)

        assert response.status_code == HTTPStatus.OK

        response = admin_client.post(
            url,
            data={
                "user": agente_imobiliario_factory().user.pk,
            },
        )
        assert response.status_code == HTTPStatus.FOUND
        assert AgenteImobiliario.objects.filter(user__username="test").exists()

    def test_view_agente(self, admin_client, agente_imobiliario_factory):
        agente = agente_imobiliario_factory()
        url = reverse(
            "admin:users_agenteimobiliario_change", kwargs={"object_id": agente.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK


class TestInquilinoAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_inquilino_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK

    def test_search(self, admin_client):
        url = reverse("admin:users_inquilino_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK

    def test_add(self, admin_client, inquilino_factory):
        url = reverse("admin:users_inquilino_add")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK

        response = admin_client.post(
            url,
            data={
                "user": inquilino_factory().pk,
            },
        )
        assert response.status_code == HTTPStatus.FOUND
        assert Inquilino.objects.filter(user__username="test").exists()

    def test_view_inquilino(self, admin_client, inquilino_factory):
        inquilino = inquilino_factory()
        url = reverse(
            "admin:users_inquilino_change", kwargs={"object_id": inquilino.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK


class TestProprietarioAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_proprietario_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK

    def test_search(self, admin_client):
        url = reverse("admin:users_proprietario_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK

    def test_add(self, admin_client, proprietario_factory):
        url = reverse("admin:users_proprietario_add")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK

        response = admin_client.post(
            url,
            data={
                "user": proprietario_factory().pk,
                "preferencias_de_busca": "example_preference",
            },
        )
        assert response.status_code == HTTPStatus.FOUND
        assert Proprietario.objects.filter(user__username="test").exists()

    def test_view_proprietario(self, admin_client, proprietario_factory):
        proprietario = proprietario_factory()
        url = reverse(
            "admin:users_proprietario_change", kwargs={"object_id": proprietario.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK
