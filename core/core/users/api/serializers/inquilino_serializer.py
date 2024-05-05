from rest_framework import serializers
from core.users.models import InquilinoProfile
from core.users.api.serializers.user_serializer import UserSerializer

class InquilinoProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = InquilinoProfile
        fields = ['user',]

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['user_type'] = 'inquilino'
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        inquilino = InquilinoProfile.objects.create(user_profile=user, **validated_data)
        return inquilino
    

class InquilinoProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Incluir informações do usuário associado
    # imoveis_gerenciados = ImovelSerializer(many=True, read_only=True)
   
    class Meta:
        model = InquilinoProfile
        fields = [
            'user', 
            # 'imoveis_gerenciados'
            ]  # Assumindo que inquilinos gerenciam ou têm imóveis associados

    def to_representation(self, instance):
        """ Personaliza a representação de saída para adicionar detalhes adicionais conforme necessário. """
        representation = super().to_representation(instance)
        # Adicione aqui mais lógica se necessário para incluir detalhes adicionais
        return representation