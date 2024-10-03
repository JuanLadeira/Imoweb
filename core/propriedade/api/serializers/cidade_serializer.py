from rest_framework import serializers

from core.propriedade.api.serializers.inlines.estado_inline_serializer import (
    EstadoInlineSerializer,
)
from core.propriedade.models import Cidade
from core.propriedade.models import Estado


class CidadePostSerializer(serializers.ModelSerializer):
    estado = serializers.PrimaryKeyRelatedField(
        queryset=Estado.objects.all(), required=True
    )

    class Meta:
        model = Cidade
        fields = "__all__"


class CidadeGetSerializer(serializers.ModelSerializer):
    estado = EstadoInlineSerializer()

    class Meta:
        model = Cidade
        fields = "__all__"
