from django.shortcuts import get_object_or_404

from .models import Post


def get_post_by_id(post_id: int) -> Post:
    return get_object_or_404(Post, id=post_id)


def create_post(data: dict) -> Post:
    return Post.objects.create(**data)


def update_post(post_id: int, data: dict) -> Post:
    post = get_post_by_id(post_id)

    for field, value in data.items():
        setattr(post, field, value)
    post.save()

    return post


def delete_post(post_id: int) -> None:
    post = get_post_by_id(post_id)
    post.delete()
