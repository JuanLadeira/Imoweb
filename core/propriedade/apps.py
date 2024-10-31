from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class PropriedadeConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "core.propriedade"
    verbose_name = _("Gestão de Imóveis")
