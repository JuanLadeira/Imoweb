from logging import getLogger

from django.db import transaction
from rest_framework import serializers

from core.users.api.serializers.user_serializer import UserSerializer
from core.users.models import AgenteImobiliario
from core.users.utils import get_especific_user_data

logger = getLogger("django")


class AgenteImobiliarioPostSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False)
    password = serializers.CharField(required=False)
    password2 = serializers.CharField(required=False)
    first_name = serializers.CharField(required=False)
    last_name = serializers.CharField(required=False)
    telefone = serializers.CharField(required=False)
    email = serializers.EmailField(required=False)
    foto = serializers.ImageField(required=False)
    endereco = serializers.CharField(required=False)

    class Meta:
        model = AgenteImobiliario
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
    def create(self, validated_data):
        user_data, validated_data = get_especific_user_data(validated_data)
        user_data["tipo"] = "agente"
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()

        return AgenteImobiliario.objects.create(user=user, **validated_data)

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data, validated_data = get_especific_user_data(validated_data)

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
        serializer = AgenteImobiliarioGetSerializer(instance)
        return serializer.data


class AgenteImobiliarioGetSerializer(serializers.ModelSerializer):
    user_id = serializers.SerializerMethodField()
    nome = serializers.SerializerMethodField()
    telefone = serializers.CharField(required=False, source="user.telefone")
    email = serializers.EmailField(required=False, source="user.email")
    foto = serializers.ImageField(required=False, source="user.foto")
    endereco = serializers.CharField(required=False, source="user.endereco")

    class Meta:
        model = AgenteImobiliario
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
