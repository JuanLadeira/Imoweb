from rest_framework import serializers

from core.propriedade.api.serializers.inlines.foto_inline_serializer import (
    FotoInlineSerializer,
)
from core.propriedade.models import Cidade
from core.propriedade.models import Imovel
from core.propriedade.models import TipoDeImovel
from core.users.models import Proprietario


class ImovelPostSerializer(serializers.ModelSerializer):
    proprietario = serializers.PrimaryKeyRelatedField(
        queryset=Proprietario.objects.all()
    )
    cidade = serializers.PrimaryKeyRelatedField(queryset=Cidade.objects.all())
    tipo = serializers.PrimaryKeyRelatedField(queryset=TipoDeImovel.objects.all())

    class Meta:
        model = Imovel
        fields = [
            "proprietario",
            "cidade",
            "tipo",
            "endereco",
            "pais",
            "cep",
            "titulo",
            "descricao",
            "tipo_de_contrato",
            "status",
            "preco",
            "preco_locacao",
            "area",
            "quartos",
            "banheiros",
            "vagas",
            "iptu",
            "condominio",
        ]


class ImovelUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = [
            "proprietario",
            "cidade",
            "tipo",
            "endereco",
            "pais",
            "cep",
            "titulo",
            "descricao",
            "tipo_de_contrato",
            "status",
            "preco",
            "preco_locacao",
            "area",
            "quartos",
            "banheiros",
            "vagas",
            "iptu",
            "condominio",
        ]


class ImovelGetSerializer(serializers.ModelSerializer):
    cidade = serializers.StringRelatedField()
    proprietario = serializers.StringRelatedField()
    criado_por = serializers.StringRelatedField()
    tipo = serializers.StringRelatedField()
    fotos = FotoInlineSerializer(many=True)

    class Meta:
        model = Imovel
        fields = "__all__"
