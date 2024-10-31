from rest_framework import serializers

from core.propriedade.models import Estado


class EstadoPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"


class EstadoGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado
        fields = "__all__"
