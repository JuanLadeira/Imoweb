from rest_framework import serializers


class ForgetPasswordSerializer(serializers.Serializer):
    """
    Serializador para requisições de recuperação de senha.
    """

    email = serializers.EmailField()
