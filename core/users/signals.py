from django.db.models.signals import post_save
from django.dispatch import receiver

from core.users.models import AgenteImobiliario
from core.users.models import Inquilino
from core.users.models import Proprietario
from core.users.models import UserType
from core.users.permissions import create_group_with_permissions


@receiver(post_save, sender=AgenteImobiliario)
@receiver(post_save, sender=Inquilino)
@receiver(post_save, sender=Proprietario)
def assign_permissions_to_user(sender, instance, created, **kwargs):
    """
    Atribui permissões ao usuário após a criação, com base no tipo de usuário.
    """
    if created:
        if isinstance(instance, AgenteImobiliario):
            user_type = UserType.AGENTE
        elif isinstance(instance, Inquilino):
            user_type = UserType.INQUILINO
        elif isinstance(instance, Proprietario):
            user_type = UserType.PROPRIETARIO
        else:
            return

        group = create_group_with_permissions(user_type)
        instance.user.groups.add(group)
