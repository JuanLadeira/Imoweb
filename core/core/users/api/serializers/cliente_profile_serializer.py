from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.users.models import ClienteProfile
from core.users.api.serializers.user_serializer import UserSerializer
from django.db import transaction

from logging import getLogger

logger = getLogger("django")

class ClienteProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClienteProfile
        fields = ['user', 'preferencias_de_busca']

    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['user_type'] = 'cliente'
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            user = user_serializer.save()
        cliente_profile = ClienteProfile.objects.create(user=user, **validated_data)
        return cliente_profile

    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user_serializer = UserSerializer(instance=user, data=user_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()

        return super().update(instance, validated_data)

class ClienteProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Usuário associado, somente leitura

    class Meta:
        model = ClienteProfile
        fields = ["id", 'user', 'preferencias_de_busca']

    def to_representation(self, instance):
        """ Customizar a representação de saída para incluir detalhes adicionais conforme necessário """
        representation = super().to_representation(instance)
        # Aqui você pode adicionar lógica adicional se precisar customizar a saída
        return representation