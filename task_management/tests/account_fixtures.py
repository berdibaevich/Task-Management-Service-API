import pytest

from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken
from apps.account.models import Account



@pytest.fixture
def get_user(db):
    user = Account.objects.create(username = 'user1')
    user.set_password("qwerty")
    user.save()
    return user


@pytest.fixture
def authenticated_client(db, get_user):
    client = APIClient()
    refresh = RefreshToken.for_user(get_user)
    client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(refresh.access_token))
    return client
