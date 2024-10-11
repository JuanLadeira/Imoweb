import pytest
from django.urls import resolve
from django.urls import reverse

pytestmark = pytest.mark.django_db


def test_estados_detail_url(estado_factory):
    estado = estado_factory()

    assert (
        reverse("propriedade:estados-detail", kwargs={"pk": estado.id})
        == f"/api/propriedades/estados/{estado.id}/"
    )

    assert (
        resolve(f"/api/propriedades/estados/{estado.id}/").view_name
        == "propriedade:estados-detail"
    )


def test_estados_create_url():
    assert reverse("propriedade:estados-list") == "/api/propriedades/estados/"
    assert resolve("/api/propriedades/estados/").view_name == "propriedade:estados-list"


def test_cidade_detail_url(cidade_factory):
    cidade = cidade_factory()

    assert (
        reverse("propriedade:cidades-detail", kwargs={"pk": cidade.id})
        == f"/api/propriedades/cidades/{cidade.id}/"
    )
    assert (
        resolve(f"/api/propriedades/cidades/{cidade.id}/").view_name
        == "propriedade:cidades-detail"
    )


def test_cidade_create_url():
    assert reverse("propriedade:cidades-list") == "/api/propriedades/cidades/"
    assert resolve("/api/propriedades/cidades/").view_name == "propriedade:cidades-list"


def test_imovel_detail_url(imovel_factory):
    imovel = imovel_factory()

    assert reverse("propriedade:imoveis-detail", kwargs={"pk": imovel.id})
    assert (
        resolve(f"/api/propriedades/imoveis/{imovel.id}/").view_name
        == "propriedade:imoveis-detail"
    )


def test_imovel_list_url():
    assert reverse("propriedade:imoveis-list") == "/api/propriedades/imoveis/"
    assert resolve("/api/propriedades/imoveis/").view_name == "propriedade:imoveis-list"


def test_foto_detail_url(foto_factory):
    foto = foto_factory()

    assert (
        reverse("propriedade:fotos-detail", kwargs={"pk": foto.id})
        == f"/api/propriedades/fotos/{foto.id}/"
    )
    assert (
        resolve(f"/api/propriedades/fotos/{foto.id}/").view_name
        == "propriedade:fotos-detail"
    )


def test_foto_create_url():
    assert reverse("propriedade:fotos-list") == "/api/propriedades/fotos/"
    assert resolve("/api/propriedades/fotos/").view_name == "propriedade:fotos-list"


def test_tipo_de_imovel_detail_url(tipo_de_imovel_factory):
    tipo = tipo_de_imovel_factory()

    assert (
        reverse("propriedade:tipos-de-imoveis-detail", kwargs={"pk": tipo.id})
        == f"/api/propriedades/tipos-de-imoveis/{tipo.id}/"
    )
    assert (
        resolve(f"/api/propriedades/tipos-de-imoveis/{tipo.id}/").view_name
        == "propriedade:tipos-de-imoveis-detail"
    )


def test_tipo_de_imovel_create_url():
    assert (
        reverse("propriedade:tipos-de-imoveis-list")
        == "/api/propriedades/tipos-de-imoveis/"
    )
    assert (
        resolve("/api/propriedades/tipos-de-imoveis/").view_name
        == "propriedade:tipos-de-imoveis-list"
    )
