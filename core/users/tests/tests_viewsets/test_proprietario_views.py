import pytest

pytestmark = pytest.mark.django_db


class TestProprietarioEndpoint:
    endpoint = "/api/users/proprietarios/"
