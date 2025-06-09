import pytest
from django.urls import reverse

from posts.models import Post

NAMESPACE = 'api-1.0.0'


@pytest.mark.django_db
def test_get_posts(client):
    response = client.get(reverse(f'{NAMESPACE}:post-list'))

    assert response.status_code == 200
    assert 'items' in response.json()


@pytest.mark.django_db
def test_create_post_success(client, post_valid_data):
    assert Post.objects.count() == 0
    response = client.post(reverse(f'{NAMESPACE}:post-create'), data=post_valid_data, content_type='application/json')

    assert response.status_code == 200
    assert response.json()['title'] == post_valid_data['title']
    assert Post.objects.count() == 1


@pytest.mark.django_db
def test_create_post_fail(client, post_invalid_data):
    assert Post.objects.count() == 0
    response = client.post(reverse(f'{NAMESPACE}:post-create'), data=post_invalid_data, content_type='application/json')

    assert response.status_code == 422
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_get_post_success(client, post):
    response = client.get(reverse(f'{NAMESPACE}:post-retrieve', args=[post.id]))
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['title'] == post.title
    assert response_body['content'] == post.content


@pytest.mark.django_db
def test_get_post_404_fail(client):
    response = client.get(reverse(f'{NAMESPACE}:post-retrieve', args=[9999999]))
    assert response.status_code == 404


@pytest.mark.django_db
def test_update_post(client, post):
    content = 'updated'
    update_data = {'content': content}
    assert post.content != content

    response = client.patch(
        reverse(f'{NAMESPACE}:post-update', args=[post.id]),
        data=update_data,
        content_type='application/json',
    )
    assert response.status_code == 200
    post.refresh_from_db()
    assert post.content == content


@pytest.mark.django_db
def test_delete_post_success(client, post):
    response = client.delete(reverse(f'{NAMESPACE}:post-delete', args=[post.id]))
    assert response.status_code == 204
    assert Post.objects.count() == 0


@pytest.mark.django_db
def test_delete_post_fail(client):
    response = client.delete(reverse(f'{NAMESPACE}:post-delete', args=[9999999]))
    assert response.status_code == 404
