from rest_framework import serializers

from core.users.api.serializers.permission_serializer import PermissionSerializer
from core.users.models import User


class UserLoggedInSerializer(serializers.ModelSerializer):
    """
    A classe UserLoggedInSerializer é responsável por serializar os dados de um usuário logado.
    """

    user_permissions = serializers.SerializerMethodField(read_only=True)
    nome = serializers.SerializerMethodField(read_only=True)
    tipo = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "is_superuser",
            "is_staff",
            "tipo",
            "email",
            "nome",
            "first_name",
            "last_name",
            "foto",
            "telefone",
            "user_permissions",
        ]

    def to_representation(self, instance: User):
        return super().to_representation(
            instance,
        )

    def get_user_permissions(self, instance: User):
        """
        Método que serializa as permissões de um usuario logado.
        """

        user_permissions = set(instance.user_permissions.all())
        group_permissions = set()
        for group in instance.groups.all():
            group_permissions.update(group.permissions.all())

        all_permissions = user_permissions | group_permissions
        view_permissions = [
            perm
            for perm in all_permissions
            if perm.codename.startswith("view_") or perm.codename.startswith("add_")
        ]
        serializer = PermissionSerializer(view_permissions, many=True)
        return serializer.data

    def get_nome(self, instance: User) -> str:
        return instance.get_full_name()

    def get_tipo(self, instance: User) -> str:
        return instance.get_tipo_display_name()
