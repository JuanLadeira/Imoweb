from logging import getLogger

from django.db import transaction
from rest_framework import serializers

from core.users.api.serializers.user_serializer import UserSerializer
from core.users.models import Proprietario

logger = getLogger("django")


class ProprietarioPostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Proprietario
        fields = ["user"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["tipo"] = "cliente"
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        return Proprietario.objects.create(user=user, **validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        if "user" not in validated_data:
            return super().update(instance, validated_data)
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


class ProprietarioGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Proprietario
        fields = ["id", "user"]

    def to_representation(self, instance):
        """
        Customizar a representação de saída para incluir,
        detalhes adicionais conforme necessário
        """
        return super().to_representation(instance)
