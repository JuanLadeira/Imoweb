import logging

import pytest
from django.forms import model_to_dict

from core.users.api.serializers.proprietario_serializer import ProprietarioGetSerializer
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioPostSerializer,
)
from core.users.api.serializers.proprietario_serializer import (
    ProprietarioUpdateSerializer,
)

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestProprietarioPostSerializer:
    def test_create_proprietario_post_serializer(self, user_factory):
        user = user_factory.build()
        user = model_to_dict(user)

        data = {
            "username": user.get("username"),
            "password": user.get("password"),
            "password2": user.get("password"),
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name"),
            "telefone": user.get("telefone"),
            "email": user.get("email"),
            "endereco": user.get("endereco"),
        }

        serializer = ProprietarioPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        agente = serializer.save()
        assert agente, serializer.errors
        assert agente.user.password != user.get(
            "password"
        ), "Senha deveria ter sido criptografada"

    def test_update_proprietario_serializer(self, user_factory, proprietario_factory):
        proprietario = proprietario_factory()
        user_new = user_factory.build()

        user_new = model_to_dict(user_new)

        data = {
            "first_name": user_new.get("first_name"),
            "last_name": user_new.get("last_name"),
            "telefone": user_new.get("telefone"),
            "email": user_new.get("email"),
            "endereco": user_new.get("endereco"),
        }

        serializer = ProprietarioUpdateSerializer
        serializer = serializer(proprietario, data=data, partial=True)
        assert serializer.is_valid(), serializer.errors
        proprietario = serializer.save()
        assert proprietario.user.first_name == data.get(
            "first_name"
        ), "deveria ser igual"

    def test_read_proprietario_get_serializer(self, proprietario_factory):
        proprietario = proprietario_factory()

        serializer = ProprietarioGetSerializer
        serializer = serializer(proprietario)

        assert (
            serializer.data.get("nome") == proprietario.user.get_full_name()
        ), "deveria ser igual"
        assert (
            serializer.data.get("user_id") == proprietario.user.id
        ), "deveria ser igual"
        assert (
            serializer.data.get("telefone") == proprietario.user.telefone
        ), "deveria ser igual"
        assert (
            serializer.data.get("email") == proprietario.user.email
        ), "deveria ser igual"
        assert (
            serializer.data.get("endereco") == proprietario.user.endereco
        ), "deveria ser igual"

    def test_response_data_proprietario_post_serializer(self, user_factory):
        user = user_factory.build()
        user = model_to_dict(user)

        data = {
            "username": user.get("username"),
            "password": user.get("password"),
            "password2": user.get("password"),
            "first_name": user.get("first_name"),
            "last_name": user.get("last_name"),
            "telefone": user.get("telefone"),
            "email": user.get("email"),
            "endereco": user.get("endereco"),
        }

        serializer = ProprietarioPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        agente = serializer.save()
        assert agente, serializer.errors
        assert agente.user.password != user.get(
            "password"
        ), "Senha deveria ter sido criptografada"

    def test_post_to_representation(self, proprietario_factory):
        proprietario = proprietario_factory()

        serializer = ProprietarioPostSerializer
        representation = serializer().to_representation(proprietario)

        expected_data = ProprietarioGetSerializer(proprietario).data

        assert (
            representation == expected_data
        ), "Representation should match expected data"

    def test_update_to_representation(self, proprietario_factory):
        proprietario = proprietario_factory()

        serializer = ProprietarioUpdateSerializer
        representation = serializer().to_representation(proprietario)

        expected_data = ProprietarioGetSerializer(proprietario).data

        assert (
            representation == expected_data
        ), "Representation should match expected data"
