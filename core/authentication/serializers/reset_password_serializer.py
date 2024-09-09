from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as djValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as drfValidationError

from core.users.api.validator import validar_senhas_coincidem


class ResetPasswordSerializer(serializers.Serializer):
    """
    Serializer para a requisição de redefinição de senha.

    Campos:
        token (CharField): Token de redefinição de senha fornecido ao usuário.
        email (EmailField): Email do usuário que deseja redefinir a senha.
        new_password (CharField): Nova senha escolhida pelo usuário.
    """

    token = serializers.CharField()
    email = serializers.EmailField()
    new_password = serializers.CharField()
    new_password_confirm = serializers.CharField()

    def validate(self, data):
        validar_senhas_coincidem(data["new_password"], data["new_password_confirm"])
        try:
            validate_password(data["new_password"])
        except djValidationError as e:
            raise drfValidationError({"password": e.messages}) from e

        return data
