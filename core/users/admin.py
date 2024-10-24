from django.contrib import admin
from unfold.admin import ModelAdmin
from unfold.admin import StackedInline

from core.users.forms.agente_form import AgenteImobiliarioChangeForm
from core.users.forms.agente_form import AgenteImobiliarioCreationForm
from core.users.forms.iniquilino_form import InquilinoChangeForm
from core.users.forms.iniquilino_form import InquilinoCreationForm
from core.users.forms.proprietario_form import ProprietarioChangeForm
from core.users.forms.proprietario_form import ProprietarioCreationForm
from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario
from core.users.models import User


class UserInline(StackedInline):
    model = User
    fields = [
        "username",
        "password",
        "email",
        "first_name",
        "last_name",
        "is_active",
        "user_permissions",
        "groups",
    ]
    extra = 0  # Defi


class UserAtivoFilter(admin.SimpleListFilter):
    title = "user ativo?"
    parameter_name = "is_active"

    def lookups(self, request, model_admin):
        return (("True", "Ativo"), ("False", "Inativo"))

    def queryset(self, request, queryset):
        match self.value():
            case "True":
                return queryset.filter(user__is_active=True)
            case "False":
                return queryset.filter(user__is_active=False)
            case _:
                return queryset


class BaseUserAdmin(ModelAdmin):
    list_display = (
        "username",
        "tipo",
        "email",
        "password",
        "first_name",
        "last_name",
        "date_joined",
        "is_active",
        "user_permissions",
        "groups",
    )
    search_fields = ("user__username", "user__email")
    readonly_fields = ["id", "tipo"]

    list_filter = (UserAtivoFilter,)

    @admin.display(description="Username")
    def username(self, obj):
        return obj.user.username

    @admin.display(description="Tipo de Usuário")
    def tipo(self, obj):
        return obj.user.tipo

    @admin.display(description="Email")
    def email(self, obj):
        return obj.user.email

    @admin.display(description="Password")
    def password(self, obj):
        return obj.user.password

    @admin.display(description="First Name")
    def first_name(self, obj):
        return obj.user.first_name

    @admin.display(description="Last Name")
    def last_name(self, obj):
        return obj.user.last_name

    @admin.display(description="Date Joined")
    def date_joined(self, obj):
        return obj.user.date_joined

    @admin.display(description="Active")
    def is_active(self, obj):
        return obj.user.is_active

    @admin.display(description="User Permissions")
    def user_permissions(self, obj):
        return obj.user.user_permissions

    @admin.display(description="Groups")
    def groups(self, obj):
        return obj.user.groups


@admin.register(Inquilino)
class InquilinoAdmin(BaseUserAdmin):
    form = InquilinoChangeForm
    add_form = InquilinoCreationForm

    def get_form(self, request, obj=None, **kwargs):
        """
        retorna o formulário correto com base na solicitação.
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        else:
            defaults["form"] = self.form

        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para salvar o User antes do Inquilino.
        """
        if change:
            # Atualizando um User existente
            user = obj.user
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.is_active = form.cleaned_data["is_active"]
            user.foto = form.cleaned_data["foto"]
            user.endereco = form.cleaned_data["endereco"]
            if form.cleaned_data["password1"]:
                user.set_password(
                    form.cleaned_data["password1"]
                )  # Atualiza a senha se for fornecida
            user.save()

        else:
            # Criando um novo User
            user_data = {
                "username": form.cleaned_data["username"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "is_active": form.cleaned_data["is_active"],
                "tipo": "inquilino",
                "foto": form.cleaned_data["foto"],
                "telefone": form.cleaned_data["telefone"],
                "endereco": form.cleaned_data["endereco"],
            }
            user = User(**user_data)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            obj.user = user

        super().save_model(request, obj, form, change)


@admin.register(AgenteImobiliario)
class AgenteImobiliarioAdmin(BaseUserAdmin):
    form = AgenteImobiliarioChangeForm
    add_form = AgenteImobiliarioCreationForm

    def get_form(self, request, obj=None, **kwargs):
        """
        retorna o formulário correto com base na solicitação.
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        else:
            defaults["form"] = self.form

        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para salvar o User antes do AgenteImobiliario.
        """
        if change:
            # Atualizando um User existente
            user = obj.user
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.is_active = form.cleaned_data["is_active"]
            user.foto = form.cleaned_data["foto"]
            user.telefone = form.cleaned_data["telefone"]
            user.endereco = form.cleaned_data["endereco"]
            if form.cleaned_data["password1"]:
                user.set_password(
                    form.cleaned_data["password1"]
                )  # Atualiza a senha se for fornecida
            user.save()

        else:
            # Criando um novo User
            user_data = {
                "username": form.cleaned_data["username"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "is_active": form.cleaned_data["is_active"],
                "tipo": "agente",
                "foto": form.cleaned_data["foto"],
                "telefone": form.cleaned_data["telefone"],
                "endereco": form.cleaned_data["endereco"],
            }
            user = User(**user_data)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            obj.user = user

        super().save_model(request, obj, form, change)


@admin.register(Proprietario)
class ProprietarioAdmin(BaseUserAdmin):
    form = ProprietarioChangeForm
    add_form = ProprietarioCreationForm

    def get_form(self, request, obj=None, **kwargs):
        """
        retorna o formulário correto com base na solicitação.
        """
        defaults = {}
        if obj is None:
            defaults["form"] = self.add_form
        else:
            defaults["form"] = self.form

        defaults.update(kwargs)
        return super().get_form(request, obj, **defaults)

    def save_model(self, request, obj, form, change):
        """
        Sobrescreve o método save_model para salvar o User antes do Proprietario.
        """
        if change:
            # Atualizando um User existente
            user = obj.user
            user.username = form.cleaned_data["username"]
            user.email = form.cleaned_data["email"]
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.is_active = form.cleaned_data["is_active"]
            user.telefone = form.cleaned_data["telefone"]
            user.foto = form.cleaned_data["foto"]
            user.endereco = form.cleaned_data["endereco"]
            if form.cleaned_data["password1"]:
                user.set_password(
                    form.cleaned_data["password1"]
                )  # Atualiza a senha se for fornecida
            user.save()

        else:
            # Criando um novo User
            user_data = {
                "username": form.cleaned_data["username"],
                "email": form.cleaned_data["email"],
                "first_name": form.cleaned_data["first_name"],
                "last_name": form.cleaned_data["last_name"],
                "is_active": form.cleaned_data["is_active"],
                "tipo": "proprietario",
                "foto": form.cleaned_data["foto"],
                "telefone": form.cleaned_data["telefone"],
                "endereco": form.cleaned_data["endereco"],
            }
            user = User(**user_data)
            user.set_password(form.cleaned_data["password1"])
            user.save()
            obj.user = user

        super().save_model(request, obj, form, change)
