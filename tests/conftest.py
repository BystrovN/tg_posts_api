import pytest
from django.test import Client
from django.contrib.auth import get_user_model

from auth.models import Token


@pytest.fixture
def client():
    return Client()


@pytest.fixture
def registration_valid_data():
    return {'username': 'username', 'password': 'password'}


@pytest.fixture
def user(registration_valid_data):
    return get_user_model().objects.create_user(**registration_valid_data)


@pytest.fixture
def token(user):
    return Token.objects.create(user=user, key=Token.generate_token())
