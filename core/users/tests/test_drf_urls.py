import pytest
from django.urls import resolve
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_agente_detail(agente_imobiliario_factory):
    agente = agente_imobiliario_factory()

    assert (
        reverse("users:agentes-detail", kwargs={"pk": agente.id})
        == f"/api/users/agentes/{agente.id}/"
    )

    assert (
        resolve(f"/api/users/agentes/{agente.id}/").view_name == "users:agentes-detail"
    )


def test_agente_list():
    assert reverse("users:agentes-list") == "/api/users/agentes/"
    assert resolve("/api/users/agentes/").view_name == "users:agentes-list"


def test_inquilino_detail(inquilino_factory):
    inquilino = inquilino_factory()

    assert (
        reverse("users:inquilinos-detail", kwargs={"pk": inquilino.id})
        == f"/api/users/inquilinos/{inquilino.id}/"
    )
    assert (
        resolve(f"/api/users/inquilinos/{inquilino.id}/").view_name
        == "users:inquilinos-detail"
    )


def test_inquilino_list():
    assert reverse("users:inquilinos-list") == "/api/users/inquilinos/"
    assert resolve("/api/users/inquilinos/").view_name == "users:inquilinos-list"


def test_proprietario_detail(proprietario_factory):
    proprietario = proprietario_factory()

    assert (
        reverse("users:proprietarios-detail", kwargs={"pk": proprietario.id})
        == f"/api/users/proprietarios/{proprietario.id}/"
    )
    assert (
        resolve(f"/api/users/proprietarios/{proprietario.id}/").view_name
        == "users:proprietarios-detail"
    )


def test_proprietario_list():
    assert reverse("users:proprietarios-list") == "/api/users/proprietarios/"
    assert resolve("/api/users/proprietarios/").view_name == "users:proprietarios-list"
