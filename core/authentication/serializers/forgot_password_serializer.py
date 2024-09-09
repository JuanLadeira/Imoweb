from rest_framework import serializers


class ForgotPasswordSerializer(serializers.Serializer):
    """
    Serializador para requisições de recuperação de senha.
    """

    email = serializers.EmailField()
