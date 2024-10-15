import contextlib

from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


# Import signals only when the app is ready
def import_signals():
    with contextlib.suppress(ImportError):
        import core.users.signals  # noqa: F401


class UsersConfig(AppConfig):
    name = "core.users"
    verbose_name = _("Users")

    def ready(self):
        import_signals()
