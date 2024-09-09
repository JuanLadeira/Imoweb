from rest_framework import serializers


class LogoutSerializer(serializers.Serializer):
    """
    Serializador para requisições de logout.

    Possui um campo para identificar qual token de refresh será invalidado.
    """

    refresh_token = serializers.CharField()

    class Meta:
        fields = ["refresh_token"]
