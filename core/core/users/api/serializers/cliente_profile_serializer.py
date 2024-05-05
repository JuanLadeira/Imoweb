from rest_framework import serializers
from core.users.models import ClienteProfile
from core.users.api.serializers.user_serializer import UserSerializer


class ClienteProfilePostSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = ClienteProfile
        fields = ['user', 'preferencias_de_busca']

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user_data['user_type'] = 'cliente'
        user = UserSerializer.create(UserSerializer(), validated_data=user_data)
        cliente_profile = ClienteProfile.objects.create(user=user, **validated_data)
        return cliente_profile

class ClienteProfileGetSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)  # Usuário associado, somente leitura

    class Meta:
        model = ClienteProfile
        fields = ['user', 'preferencias_de_busca']

    def to_representation(self, instance):
        """ Customizar a representação de saída para incluir detalhes adicionais conforme necessário """
        representation = super().to_representation(instance)
        # Aqui você pode adicionar lógica adicional se precisar customizar a saída
        return representation