from rest_framework import serializers

from core.propriedade.models import Foto
from core.propriedade.models import Imovel


class FotoPostSerializer(serializers.ModelSerializer):
    imovel = serializers.PrimaryKeyRelatedField(
        queryset=Imovel.objects.all(), required=True
    )
    foto = serializers.ImageField()

    class Meta:
        model = Foto
        fields = "__all__"
