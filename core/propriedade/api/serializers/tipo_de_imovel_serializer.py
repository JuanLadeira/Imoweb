from rest_framework import serializers

from core.propriedade.models import TipoDeImovel


class TipoDeImovelPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeImovel
        fields = "__all__"


class TipoDeImovelGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TipoDeImovel
        fields = "__all__"
