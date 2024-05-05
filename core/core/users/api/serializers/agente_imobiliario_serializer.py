from rest_framework import serializers
from core.users.models import AgenteImobiliarioProfile
from core.users.api.serializers.user_serializer import UserSerializer

class AgenteImobiliarioProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = AgenteImobiliarioProfile
        fields = ['user']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['user_type'] = 'agente'
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        agente_profile = AgenteImobiliarioProfile.objects.create(user_profile=user, **validated_data)
        return agente_profile
    

class AgenteImobiliarioProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    # imoveis_gerenciados = ImovelSerializer(many=True, read_only=True)

    class Meta:
        model = AgenteImobiliarioProfile
        fields = [
            'user', 
            # 'imoveis_gerenciados'
            ]