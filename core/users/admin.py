from django.contrib import admin
from guardian.admin import GuardedModelAdmin

from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario


class BaseUserAdmin(GuardedModelAdmin):
    @admin.display(
        description="Username",
    )
    def user_username(self, obj):
        return obj.user.username

    @admin.display(
        description="Tipo de Usuário",
    )
    def user_tipo(self, obj):
        return obj.user.tipo

    @admin.display(
        description="Email",
    )
    def user_email(self, obj):
        return obj.user.email

    @admin.display(
        description="Password",
    )
    def user_password(self, obj):
        return obj.user.password

    @admin.display(
        description="First Name",
    )
    def user_first_name(self, obj):
        return obj.user.first_name

    @admin.display(
        description="Last Name",
    )
    def user_last_name(self, obj):
        return obj.user.last_name

    @admin.display(
        description="Date Joined",
    )
    def user_date_joined(self, obj):
        return obj.user.date_joined

    @admin.display(
        description="Active",
    )
    def user_is_active(self, obj):
        return obj.user.is_active

    @admin.display(
        description="User Permissions",
    )
    def user_user_permissions(self, obj):
        return obj.user.user_permissions

    @admin.display(
        description="Groups",
    )
    def user_groups(self, obj):
        return obj.user.groups


# Register your models here.
@admin.register(AgenteImobiliario)
class AgenteAdmin(BaseUserAdmin):
    list_display = (
        "user_username",
        "user_tipo",
        "user_email",
        "user_password",
        "user_first_name",
        "user_last_name",
        "user_date_joined",
        "user_is_active",
        "user_user_permissions",
        "user_groups",
    )


@admin.register(Inquilino)
class InquilinoAdmin(BaseUserAdmin):
    list_display = (
        "user_username",
        "user_tipo",
        "user_email",
        "user_password",
        "user_first_name",
        "user_last_name",
        "user_date_joined",
        "user_is_active",
        "user_user_permissions",
        "user_groups",
    )


@admin.register(Proprietario)
class ProprietarioAdmin(BaseUserAdmin):
    list_display = (
        "user_username",
        "user_tipo",
        "user_email",
        "user_password",
        "user_first_name",
        "user_last_name",
        "user_date_joined",
        "user_is_active",
        "user_user_permissions",
        "user_groups",
        "preferencias_de_busca",
    )
