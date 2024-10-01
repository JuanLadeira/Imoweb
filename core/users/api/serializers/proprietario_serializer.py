from logging import getLogger
from typing import Any

from django.db import transaction
from rest_framework import serializers

from core.users.api.serializers.user_serializer import UserSerializer
from core.users.models import Proprietario

logger = getLogger("django")


class ProprietarioPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, source="user.username")
    password = serializers.CharField(required=False, source="user.password")
    password2 = serializers.CharField(
        required=False, source="user.password2", write_only=True
    )
    first_name = serializers.CharField(required=False, source="user.first_name")
    last_name = serializers.CharField(required=False, source="user.last_name")
    telefone = serializers.CharField(required=False, source="user.telefone")
    email = serializers.EmailField(required=False, source="user.email")
    foto = serializers.ImageField(required=False, source="user.foto")
    endereco = serializers.CharField(required=False, source="user.endereco")

    class Meta:
        model = Proprietario
        fields = [
            "username",
            "password",
            "password2",
            "first_name",
            "last_name",
            "telefone",
            "email",
            "foto",
            "endereco",
        ]

    @transaction.atomic
    def create(self, validated_data: dict[str, Any]):
        user_data = validated_data.pop("user")
        user_data["tipo"] = "proprietario"
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

        return Proprietario.objects.create(user=user, **validated_data)

    def to_representation(self, instance):
        serializer = ProprietarioGetSerializer(instance)
        return serializer.data


class ProprietarioUpdateSerializer(serializers.ModelSerializer):
    first_name = serializers.CharField(required=False, source="user.first_name")
    last_name = serializers.CharField(required=False, source="user.last_name")
    telefone = serializers.CharField(required=False, source="user.telefone")
    email = serializers.EmailField(required=False, source="user.email")
    foto = serializers.ImageField(required=False, source="user.foto")
    endereco = serializers.CharField(required=False, source="user.endereco")

    class Meta:
        model = Proprietario
        fields = [
            "first_name",
            "last_name",
            "telefone",
            "email",
            "foto",
            "endereco",
        ]

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

    def to_representation(self, instance):
        serializer = ProprietarioGetSerializer(instance)
        return serializer.data


class ProprietarioGetSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    nome = serializers.SerializerMethodField()
    telefone = serializers.CharField(required=False, source="user.telefone")
    email = serializers.EmailField(required=False, source="user.email")
    foto = serializers.ImageField(required=False, source="user.foto")
    endereco = serializers.CharField(required=False, source="user.endereco")

    class Meta:
        model = Proprietario
        fields = [
            "id",
            "user_id",
            "nome",
            "telefone",
            "email",
            "foto",
            "endereco",
        ]

    def get_nome(self, obj):
        return obj.user.get_full_name()

    def get_user_id(self, obj):
        return obj.user.id
