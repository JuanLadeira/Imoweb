# ruff: noqa: S106

import pytest
from django.test import Client
from pytest_factoryboy import register
from rest_framework.test import APIClient

from core.users.tests.factories import AgenteImobiliarioFactory
from core.users.tests.factories import InquilinoFactory
from core.users.tests.factories import ProprietarioFactory
from core.users.tests.factories import UserFactory


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
def api_client():
    return APIClient()


@pytest.fixture()
def client():
    return Client()


register(UserFactory)
register(ProprietarioFactory)
register(InquilinoFactory)
register(AgenteImobiliarioFactory)
