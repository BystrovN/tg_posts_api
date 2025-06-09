from ninja import ModelSchema
from pydantic import constr

from .models import Post


class PostInSchema(ModelSchema):
    title: constr(min_length=1)
    content: constr(min_length=1)

    class Meta:
        model = Post
        fields = ('title', 'content')


class PostOutSchema(ModelSchema):

    class Meta:
        model = Post
        fields = ('id', 'title', 'content', 'created_at', 'updated_at')
