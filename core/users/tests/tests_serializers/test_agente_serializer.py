import logging

import pytest
from django.forms import model_to_dict

from core.users.api.serializers.agente_imobiliario_serializer import (
    AgenteImobiliarioPostSerializer,
)

logger = logging.getLogger(__name__)


@pytest.mark.django_db()
class TestAgenteImobiliarioPostSerializer:
    def test_create_agente_imobiliario_post_serializer(self, user_factory):
        user = user_factory.build()
        user = model_to_dict(user)
        user.pop("id")

        logging.info(user)

        serializer = AgenteImobiliarioPostSerializer
        serializer = serializer(data={"user": user})
        assert serializer.is_valid(), serializer.errors
        assert serializer.save(), serializer.errors
        assert serializer.data, serializer.errors

    def test_update_agente_imobiliario_post_serializer(self, user_factory):
        user = user_factory.build()
        user = model_to_dict(user)
        user.pop("id")

        logging.info(user)

        serializer = AgenteImobiliarioPostSerializer
        serializer = serializer(data={"user": user})
        assert serializer.is_valid(), serializer.errors
        assert serializer.save(), serializer.errors
        assert serializer.data, serializer.errors
