import pytest

pytestmark = pytest.mark.django_db


class TestInquilinoEndpoint:
    endpoint = "/api/users/inquilinos/"
