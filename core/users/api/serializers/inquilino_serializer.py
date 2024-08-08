import logging

from django.db import transaction
from rest_framework import serializers

from core.users.api.serializers.user_serializer import UserSerializer
from core.users.models import InquilinoProfile

logger = logging.getLogger("django")


class InquilinoProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = InquilinoProfile
        fields = ["user"]

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop("user")
        user_data["user_type"] = "inquilino"
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        return InquilinoProfile.objects.create(user=user, **validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop("user")
        user = instance.user

        user_serializer = UserSerializer(instance=user, data=user_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()

        return super().update(instance, validated_data)


class InquilinoProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = InquilinoProfile
        fields = [
            "id",
            "user",
        ]

    def to_representation(self, instance):
        """
        Personaliza a representação de saída para adicionar
        detalhes adicionais conforme necessário.
        """
        return super().to_representation(instance)