from rest_framework import serializers

from core.propriedade.models import Estado


class EstadoInlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"
