# Importe outras fábricas que você deseja usar
import logging

from django.conf import settings
from django.core.management.base import BaseCommand

from core.users.models import User
from core.users.tests.factories import AgenteImobiliarioFactory
from core.users.tests.factories import InquilinoFactory
from core.users.tests.factories import ProprietarioFactory
from core.users.tests.factories import UserFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    help = "Cria dados iniciais para testar a aplicação"

    def handle(self, *args, **kwargs):
        logging.basicConfig(level=logging.INFO)

        if settings.DEBUG:
            self.stdout.write("Criando dados iniciais para testar a aplicação")
            if not User.objects.filter(username="admin").exists():
                self.stdout.write("Criando usuário admin")
                user = UserFactory.create(
                    username="admin",
                    email="admin@admin.com",
                    is_superuser=True,
                    is_staff=True,
                )
                user.set_password("admin")
                AgenteImobiliarioFactory.create(user=user)

            AgenteImobiliarioFactory.create_batch(10)
            ProprietarioFactory.create_batch(10)
            InquilinoFactory.create_batch(10)

            self.stdout.write("Dados iniciais criados com sucesso")
        else:
            self.stdout.write("O comando só pode ser executado em modo DEBUG")
