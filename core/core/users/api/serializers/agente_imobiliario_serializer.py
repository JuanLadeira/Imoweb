from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from core.users.models import AgenteImobiliarioProfile
from core.users.api.serializers.user_serializer import UserSerializer
from logging import getLogger
from django.db import transaction

logger = getLogger("django")

class AgenteImobiliarioProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AgenteImobiliarioProfile
        fields = ['user']
        
    @transaction.atomic
    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['user_type'] = 'agente'
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid(raise_exception=True):
            logger.info("passei na validação, criando usuário")
            user = user_serializer.save()
        try:
            agente_profile = AgenteImobiliarioProfile.objects.create(user=user, **validated_data)
        except:
            logger.error("Erro ao criar perfil de agente")
        return agente_profile
    
    @transaction.atomic
    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        user = instance.user

        user_serializer = UserSerializer(instance=user, data=user_data, partial=True)
        if user_serializer.is_valid(raise_exception=True):
            user_serializer.save()

        return super().update(instance, validated_data)

class AgenteImobiliarioProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # imoveis_gerenciados = ImovelSerializer(many=True, read_only=True)

    class Meta:
        model = AgenteImobiliarioProfile
        fields = [
            "id",
            'user', 
            # 'imoveis_gerenciados'
            ]