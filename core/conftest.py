import pytest
from pytest_factoryboy import register

from core.users.tests.factories import AgenteImobiliarioFactory
from core.users.tests.factories import InquilinoFactory
from core.users.tests.factories import ProprietarioFactory


@pytest.fixture(autouse=True)
def _media_storage(settings, tmpdir) -> None:
    settings.MEDIA_ROOT = tmpdir.strpath


register(ProprietarioFactory)
register(InquilinoFactory)
register(AgenteImobiliarioFactory)
