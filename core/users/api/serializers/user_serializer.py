from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as djValidationError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError as drfValidationError

from core.users.models import User


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = [
            "username",
            "password",
            "password2",
            "first_name",
            "last_name",
            "tipo",
            "telefone",
            "email",
            "foto",
            "endereco",
        ]

    def validate_password(self, value):
        """
        Método que valida a senha de um usuário.
        """
        if password2 := self.initial_data.get("password2"):
            if value != password2:
                raise drfValidationError({"password": "As senhas não coincidem."})

        try:
            validate_password(value)
        except djValidationError as e:
            raise drfValidationError({"password": e.messages}) from e

        return value

    def create(self, validated_data):
        _ = validated_data.pop("password2")
        password = validated_data.pop("password")
        user = User.objects.create_user(**validated_data)
        user.set_password(password)
        return user

    def update(self, instance, validated_data):
        if "password2" in validated_data:
            _ = validated_data.pop("password2")
        return super().update(instance, validated_data)
