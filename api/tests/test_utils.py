from api.utils import get_token
from rest_framework.authtoken.models import Token
import pytest


@pytest.mark.django_db
def test_get_token():
    """Tests if get_token() function returns token."""
    token = get_token()
    assert type(token) == Token
