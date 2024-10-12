# permissions.py

import logging

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework.permissions import SAFE_METHODS
from rest_framework.permissions import BasePermission

from core.users.models import UserType

log = logging.getLogger(__name__)

# Mapas de permissões
AGENTE_IMOBILIARIO_PERMISSIONS = {
    "users.Proprietario": ["view", "add", "change", "delete"],
    "users.Inquilino": ["view", "add", "change", "delete"],
    "users.AgenteImobiliario": ["view", "change"],
    "users.User": ["change_self"],  # Permissão para alterar a si mesmo
    "propriedade.Imovel": ["view", "add", "change", "delete"],
    "propriedade.Cidade": ["view", "add", "change", "delete"],
    "propriedade.Estado": ["view", "add", "change", "delete"],
    "propriedade.TipoDeImovel": ["view", "add", "change", "delete"],
    "propriedade.Foto": ["view", "add", "change", "delete"],
}

INQUILINO_PERMISSIONS = {
    "users.User": ["change_self", "view_self"],  # Permissão para alterar a si mesmo
    "propriedade.Imovel": ["view"],
    "propriedade.Cidade": ["view"],
    "propriedade.Estado": ["view"],
    "propriedade.TipoDeImovel": ["view"],
    "propriedade.Foto": ["view"],
}

PROPRIETARIO_PERMISSIONS = {
    "users.User": ["change_self", "view_self"],  # Permissão para alterar a si mesmo
    "propriedade.Imovel": ["view", "add", "change", "delete"],
    "propriedade.Cidade": ["view"],
    "propriedade.Estado": ["view"],
    "propriedade.TipoDeImovel": ["view"],
    "propriedade.Foto": ["view"],
}

PERMISSIONS_MAP = {
    UserType.AGENTE.value: AGENTE_IMOBILIARIO_PERMISSIONS,
    UserType.INQUILINO.value: INQUILINO_PERMISSIONS,
    UserType.PROPRIETARIO.value: PROPRIETARIO_PERMISSIONS,
}


def create_group_with_permissions(user_type):
    """
    Verifica se um grupo já existe e, se não existir, cria o grupo e atribui as permissões específicas a ele.
    """
    group_name = user_type.label
    group, created = Group.objects.get_or_create(name=group_name)

    if created:
        permissions_map = PERMISSIONS_MAP.get(user_type.value, None)
        if not permissions_map:
            return group
        for model, actions in permissions_map.items():
            app_label, model_name = model.rsplit(".", 1)
            try:
                content_type = ContentType.objects.get(
                    app_label=app_label, model=model_name.lower()
                )
                for action in actions:
                    codename = f"{action}_{model_name.lower()}"
                    permission, _ = Permission.objects.get_or_create(
                        content_type=content_type,
                        codename=codename,
                        defaults={"name": f"Can {action} {model_name}"},
                    )
                    group.permissions.add(permission)
            except ContentType.DoesNotExist:
                log.exception("ContentType não encontrado)")
    return group


class IsOwnerOrReadOnly(BasePermission):
    """
    Permissão customizada para permitir que apenas os donos de um objeto possam editá-lo.
    """

    def has_object_permission(self, request, view, obj):
        # Permissões de leitura são permitidas para qualquer requisição
        if request.method in SAFE_METHODS:
            return True

        # Permissões de escrita são permitidas apenas para o dono do objeto
        return obj.user == request.user
