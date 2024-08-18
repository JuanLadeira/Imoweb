from http import HTTPStatus
from logging import getLogger

import pytest
from django.urls import reverse

from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario

log = getLogger(__name__)


@pytest.mark.django_db()
def test_admin_client_authenticated(admin_client):
    url = reverse("admin:index")
    response = admin_client.get(url)
    assert response.status_code == HTTPStatus.OK, response.status_code


@pytest.mark.django_db()
class TestAgenteAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_agenteimobiliario_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_search(self, admin_client, agente_imobiliario_factory, user_factory):
        user = user_factory(username="test")
        agente_imobiliario_factory(user=user)
        url = reverse("admin:users_agenteimobiliario_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_add(self, admin_client, agente_imobiliario_factory):
        url = reverse("admin:users_agenteimobiliario_add")
        response = admin_client.get(url)

        assert response.status_code == HTTPStatus.OK
        agente = agente_imobiliario_factory.build()
        response = admin_client.post(
            url,
            data={
                "username": agente.user.username,
                "password1": "test123!",
                "password2": "test123!",
                "email": agente.user.email,
                "first_name": agente.user.first_name,
                "last_name": agente.user.last_name,
                "is_active": agente.user.is_active,
                "endereco": "endereco",
            },
        )
        assert response.status_code == HTTPStatus.FOUND, response.status_code
        assert AgenteImobiliario.objects.filter(
            user__username=agente.user.username
        ).exists()

    def test_view_agente(self, admin_client, agente_imobiliario_factory):
        agente = agente_imobiliario_factory()
        url = reverse(
            "admin:users_agenteimobiliario_change", kwargs={"object_id": agente.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code


@pytest.mark.django_db()
class TestInquilinoAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_inquilino_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_search(self, admin_client, inquilino_factory, user_factory):
        user = user_factory(username="test")
        inquilino_factory(user=user)
        url = reverse("admin:users_inquilino_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_add(self, admin_client, inquilino_factory):
        url = reverse("admin:users_inquilino_add")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code
        inquilino = inquilino_factory.build()
        response = admin_client.post(
            url,
            data={
                "username": inquilino.user.username,
                "password1": "test123!",
                "password2": "test123!",
                "email": inquilino.user.email,
                "first_name": inquilino.user.first_name,
                "last_name": inquilino.user.last_name,
                "is_active": inquilino.user.is_active,
                "contato": "contato",
                "endereco": "endereco",
            },
        )
        assert response.status_code == HTTPStatus.FOUND, response.status_code
        assert Inquilino.objects.filter(user__username=inquilino.user.username).exists()

    def test_view_inquilino(self, admin_client, inquilino_factory):
        inquilino = inquilino_factory()
        url = reverse(
            "admin:users_inquilino_change", kwargs={"object_id": inquilino.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code


@pytest.mark.django_db()
class TestProprietarioAdmin:
    def test_changelist(self, admin_client):
        url = reverse("admin:users_proprietario_changelist")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_search(self, admin_client, proprietario_factory, user_factory):
        user = user_factory(username="test")
        proprietario_factory(user=user)
        url = reverse("admin:users_proprietario_changelist")
        response = admin_client.get(url, data={"q": "test"})
        assert response.status_code == HTTPStatus.OK, response.status_code

    def test_add(self, admin_client, proprietario_factory):
        url = reverse("admin:users_proprietario_add")
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code
        proprietario = proprietario_factory.build()
        response = admin_client.post(
            url,
            data={
                "username": proprietario.user.username,
                "password1": "test123!",
                "password2": "test123!",
                "email": proprietario.user.email,
                "first_name": proprietario.user.first_name,
                "last_name": proprietario.user.last_name,
                "is_active": proprietario.user.is_active,
                "contato": "contato",
                "endereco": "endereco",
            },
        )
        assert response.status_code == HTTPStatus.FOUND, response.status_code
        assert Proprietario.objects.filter(
            user__username=proprietario.user.username
        ).exists()

    def test_view_proprietario(self, admin_client, proprietario_factory):
        proprietario = proprietario_factory()
        url = reverse(
            "admin:users_proprietario_change", kwargs={"object_id": proprietario.pk}
        )
        response = admin_client.get(url)
        assert response.status_code == HTTPStatus.OK, response.status_code
