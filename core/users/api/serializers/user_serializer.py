from rest_framework import serializers

from core.users.models import User


class UserSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = [
            "username",
            "first_name",
            "last_name",
            "full_name",
            "user_type",
            "contato",
            "endereco",
        ]

    def get_full_name(self, obj) -> str:
        return obj.get_full_name()
