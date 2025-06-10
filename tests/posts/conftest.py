import pytest

from posts.models import Post


@pytest.fixture
def post_valid_data():
    return {'title': 'title', 'content': 'content'}


@pytest.fixture
def post_invalid_data():
    return {'title': 'title'}


@pytest.fixture
def post(post_valid_data):
    return Post.objects.create(**post_valid_data)
