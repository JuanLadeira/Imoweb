from rest_framework import serializers

from core.propriedade.models import Foto


class FotoInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foto
        exclude = ["imovel"]
