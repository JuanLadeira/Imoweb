from logging import getLogger

from django.db import transaction
from rest_framework import serializers

from core.users.api.serializers.user_serializer import UserSerializer
from core.users.models import ClienteProfile

logger = getLogger("django")


class ClienteProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClienteProfile
        fields = ["user", "preferencias_de_busca"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["user_type"] = "cliente"
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        return ClienteProfile.objects.create(user=user, **validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user

        user_serializer = UserSerializer(
            instance=user,
            data=user_data,
            partial=True,
        )
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()

        return super().update(instance, validated_data)


class ClienteProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = ClienteProfile
        fields = ["id", "user", "preferencias_de_busca"]

    def to_representation(self, instance):
        """
        Customizar a representação de saída para incluir,
        detalhes adicionais conforme necessário
        """
        return super().to_representation(instance)
