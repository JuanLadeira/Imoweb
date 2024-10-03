from rest_framework import serializers

from core.propriedade.models import Cidade


class CidadeInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cidade
        fields = "__all__"
