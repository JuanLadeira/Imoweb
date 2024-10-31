from rest_framework import serializers

from core.propriedade.api.serializers.inlines.foto_inline_serializer import (
    FotoInlineSerializer,
)
from core.propriedade.models import Imovel


class ImovelInlineSerializer(serializers.ModelSerializer):
    cidade = serializers.StringRelatedField()
    tipo = serializers.StringRelatedField()
    fotos = FotoInlineSerializer(many=True)

    class Meta:
        model = Imovel
        exclude = ["proprietario", "criado_por"]
