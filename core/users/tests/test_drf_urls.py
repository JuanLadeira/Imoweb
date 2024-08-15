import pytest
from django.urls import resolve
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_agente_detail(agente_imobiliario_factory):
    agente = agente_imobiliario_factory()
    assert (
        reverse("api:agentes-detail", kwargs={"pk": agente.id})
        == f"/api/agentes/{agente.id}/"
    )
    assert resolve(f"/api/agentes/{agente.id}/").view_name == "api:agentes-detail"


def test_agente_list():
    assert reverse("api:agentes-list") == "/api/agentes/"
    assert resolve("/api/agentes/").view_name == "api:agentes-list"
