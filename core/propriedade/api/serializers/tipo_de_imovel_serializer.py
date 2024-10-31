from rest_framework import serializers

from core.propriedade.api.serializers.inlines import imovel_inline_serializer
from core.propriedade.models import TipoDeImovel


class TipoDeImovelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeImovel
        fields = "__all__"


class TipoDeImovelGetSerializer(serializers.ModelSerializer):
    imoveis = imovel_inline_serializer.ImovelInlineSerializer(
        many=True, source="imoveis_tipo"
    )

    class Meta:
        model = TipoDeImovel
        fields = "__all__"
