import logging

import pytest
from django.forms import model_to_dict

from core.users.api.serializers.inquilino_serializer import InquilinoGetSerializer
from core.users.api.serializers.inquilino_serializer import InquilinoPostSerializer

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestInquilinoPostSerializer:
    def test_create_inquilino_post_serializer(self, user_factory):
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

        serializer = InquilinoPostSerializer
        serializer = serializer(data=data)
        assert serializer.is_valid(), serializer.errors
        inquilino = serializer.save()
        assert inquilino, serializer.errors
        assert inquilino.user.password != user.get(
            "password"
        ), "Senha deveria ter sido criptografada"

    def test_update_inquilino_post_serializer(self, user_factory, inquilino_factory):
        inquilino = inquilino_factory()
        user_new = user_factory.build()

        user_new = model_to_dict(user_new)

        data = {
            "first_name": user_new.get("first_name"),
            "last_name": user_new.get("last_name"),
            "telefone": user_new.get("telefone"),
            "email": user_new.get("email"),
            "endereco": user_new.get("endereco"),
        }

        serializer = InquilinoPostSerializer
        serializer = serializer(inquilino, data=data, partial=True)
        assert serializer.is_valid(), serializer.errors
        inquilino = serializer.save()
        assert inquilino.user.first_name == data.get("first_name"), serializer.errors

    def test_read_inquilino_get_serializer(self, inquilino_factory):
        inquilino = inquilino_factory()

        serializer = InquilinoGetSerializer
        serializer = serializer(inquilino)

        assert (
            serializer.data.get("nome") == inquilino.user.get_full_name()
        ), "deveria ser igual"
        assert serializer.data.get("user_id") == inquilino.user.id, "deveria ser igual"
        assert (
            serializer.data.get("telefone") == inquilino.user.telefone
        ), "deveria ser igual"
        assert serializer.data.get("email") == inquilino.user.email, "deveria ser igual"
        assert (
            serializer.data.get("endereco") == inquilino.user.endereco
        ), "deveria ser igual"
