# ruff: noqa: S106
import logging
from collections.abc import Generator

import pytest
from django.test import Client
from pytest_factoryboy import register
from rest_framework.test import APIClient

from core.propriedade.tests.factories import CidadeFactory
from core.propriedade.tests.factories import EstadoFactory
from core.propriedade.tests.factories import FotoFactory
from core.propriedade.tests.factories import ImovelFactory
from core.propriedade.tests.factories import TipoDeImovelFactory
from core.users.tests.factories import AgenteImobiliarioFactory
from core.users.tests.factories import InquilinoFactory
from core.users.tests.factories import ProprietarioFactory
from core.users.tests.factories import UserFactory

log = logging.getLogger(__name__)


register(UserFactory)
register(ProprietarioFactory)
register(InquilinoFactory)
register(AgenteImobiliarioFactory)
register(ImovelFactory)
register(EstadoFactory)
register(CidadeFactory)
register(TipoDeImovelFactory)
register(FotoFactory)


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.mark.django_db()
@pytest.fixture()
def admin_client(client, user_factory):
    admin_user = user_factory(username="admin", is_staff=True, is_superuser=True)
    admin_user.set_password("test123")
    admin_user.save()

    assert admin_user.is_staff, "Admin user is not staff"

    login_sucess = client.login(username="admin", password="test123")
    assert login_sucess, "Admin login failed"
    return client


@pytest.fixture()
def agente_logado(
    api_client, agente_imobiliario_factory, user_factory
) -> Generator[dict, None, None]:
    user = user_factory(is_superuser=False)
    user.set_password("password")
    user.save()

    agente = agente_imobiliario_factory(
        user=user,
    )
    agente.save()
    response = api_client.post(
        "/api/auth/token/",
        {
            "username": agente.user.username,
            "password": "password",
        },
        format="json",
    )

    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")
    yield {
        "api_client": api_client,
        "agente": agente,
        "access": token,
        "refresh": response.data["refresh"],
    }
    api_client.credentials()


@pytest.fixture()
def inquilino_logado(
    api_client, inquilino_factory, user_factory
) -> Generator[dict, None, None]:
    user = user_factory(is_superuser=False)
    user.set_password("password")
    user.save()

    inquilino = inquilino_factory(
        user=user,
    )
    inquilino.save()
    response = api_client.post(
        "/api/auth/token/",
        {
            "username": inquilino.user.username,
            "password": "password",
        },
        format="json",
    )
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")
    yield {
        "api_client": api_client,
        "inquilino": inquilino,
        "access": token,
        "refresh": response.data["refresh"],
    }

    api_client.credentials()


@pytest.fixture()
def proprietario_logado(
    api_client, proprietario_factory, user_factory
) -> Generator[dict, None, None]:
    user = user_factory(is_superuser=False)
    user.set_password("password")
    user.save()

    proprietario = proprietario_factory(
        user=user,
    )
    proprietario.save()
    response = api_client.post(
        "/api/auth/token/",
        {
            "username": proprietario.user.username,
            "password": "password",
        },
        format="json",
    )
    log.info(response.data)
    token = response.data["access"]
    api_client.credentials(HTTP_AUTHORIZATION=f"JWT {token}")
    yield {
        "api_client": api_client,
        "proprietario": proprietario,
        "access": response.data["access"],
        "refresh": response.data["refresh"],
    }
    api_client.credentials()


@pytest.fixture()
def api_client():
    return APIClient()


@pytest.fixture()
def client():
    return Client()
