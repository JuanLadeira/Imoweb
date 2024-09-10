# permissions.py

import logging

from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from core.users.models import UserType

log = logging.getLogger(__name__)

# Mapas de permissões
AGENTE_IMOBILIARIO_PERMISSIONS = {
    "users.Proprietario": ["view", "add", "change", "delete"],
    "users.Inquilino": ["view", "add", "change", "delete"],
    "users.User": ["change_self"],  # Permissão para alterar a si mesmo
}

INQUILINO_PERMISSIONS = {
    "users.User": ["change_self"],  # Permissão para alterar a si mesmo
}

PROPRIETARIO_PERMISSIONS = {
    "users.User": ["change_self"],  # Permissão para alterar a si mesmo
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
    group_name = user_type.display_name
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
                        defaults={"name": "Can {} {}"}.format(action, model_name),
                    )
                    group.permissions.add(permission)
            except ContentType.DoesNotExist:
                log.exception("ContentType não encontrado)")
    return group
