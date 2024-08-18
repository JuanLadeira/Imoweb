import pytest

pytestmark = pytest.mark.django_db


class TestAgenteEndpoint:
    endpoint = "/api/users/agentes/"
