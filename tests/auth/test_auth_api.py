import pytest
from django.urls import reverse

NAMESPACE = 'api-1.0.0'


@pytest.mark.django_db
def test_register_user_success(client, registration_valid_data):
    response = client.post(
        reverse(f'{NAMESPACE}:token-create'), data=registration_valid_data, content_type='application/json'
    )

    assert response.status_code == 201
    assert 'token' in response.json()


@pytest.mark.django_db
def test_register_user_duplicate(client, user, registration_valid_data):
    response = client.post(
        reverse(f'{NAMESPACE}:token-create'), data=registration_valid_data, content_type='application/json'
    )

    assert response.status_code == 400
    assert 'error' in response.json()


@pytest.mark.django_db
def test_get_token_success(client, user, registration_valid_data):
    response = client.post(
        reverse(f'{NAMESPACE}:token-retrieve'), data=registration_valid_data, content_type='application/json'
    )

    assert response.status_code == 200
    assert 'token' in response.json()


@pytest.mark.django_db
def test_get_token_invalid_credentials(client):
    response = client.post(
        reverse(f'{NAMESPACE}:token-retrieve'),
        data={'username': 'john', 'password': 'wrongpass'},
        content_type='application/json',
    )

    assert response.status_code == 401
    assert 'error' in response.json()
