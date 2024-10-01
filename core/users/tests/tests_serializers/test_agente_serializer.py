import logging

import pytest
from django.forms import model_to_dict

from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioGetSerializer,
)
from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioPostSerializer,
)
from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioUpdateSerializer,
)

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestAgenteImobiliarioPostSerializer:
    def test_create_agente_imobiliario_post_serializer(self, user_factory):
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

        serializer = AgenteImobiliarioPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        agente = serializer.save()
        assert agente, serializer.errors
        assert agente.user.password != user.get(
            "password"
        ), "Senha deveria ter sido criptografada"

    def test_update_agente_imobiliario_update_serializer(
        self, user_factory, agente_imobiliario_factory
    ):
        agente = agente_imobiliario_factory()
        user_new = user_factory.build()

        user_new = model_to_dict(user_new)

        user_data = {
            "first_name": user_new.get("first_name"),
            "last_name": user_new.get("last_name"),
            "telefone": user_new.get("telefone"),
            "email": user_new.get("email"),
            "endereco": user_new.get("endereco"),
        }

        serializer = AgenteImobiliarioUpdateSerializer
        serializer = serializer(agente, data=user_data, partial=True)
        assert serializer.is_valid(), serializer.errors
        agente = serializer.save()
        assert agente.user.first_name == user_data.get("first_name"), serializer.errors

    def test_read_agente_get_serializer(self, agente_imobiliario_factory):
        agente = agente_imobiliario_factory()

        serializer = AgenteImobiliarioGetSerializer
        serializer = serializer(agente)

        assert (
            serializer.data.get("nome") == agente.user.get_full_name()
        ), "deveria ser igual"
        assert serializer.data.get("user_id") == agente.user.id, "deveria ser igual"
        assert (
            serializer.data.get("telefone") == agente.user.telefone
        ), "deveria ser igual"
        assert serializer.data.get("email") == agente.user.email, "deveria ser igual"
        assert (
            serializer.data.get("endereco") == agente.user.endereco
        ), "deveria ser igual"
