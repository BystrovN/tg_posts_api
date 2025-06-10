from ninja import PatchDict, Router
from ninja.pagination import paginate
from ninja.responses import Response

from .schemas import PostInSchema, PostOutSchema
from .models import Post
from . import crud
from auth.auth_backend import TokenAuth

router = Router(tags=['Posts'])
auth = TokenAuth()


@router.get('/', response=list[PostOutSchema], url_name='post-list')
@paginate
def get_posts(request):
    return Post.objects.all()


@router.post('/', response=PostOutSchema, url_name='post-create', auth=auth)
def create_post(request, data: PostInSchema):
    return crud.create_post(data.model_dump())


@router.get('/{post_id}/', response=PostOutSchema, url_name='post-retrieve')
def get_post(request, post_id: int):
    return crud.get_post_by_id(post_id)


@router.patch('/{post_id}/', response=PostOutSchema, url_name='post-update', auth=auth)
def update_post(request, post_id: int, data: PatchDict[PostInSchema]):
    return crud.update_post(post_id, data)


@router.delete('/{post_id}/', response={204: None, 404: dict}, url_name='post-delete', auth=auth)
def delete_post(request, post_id: int):
    crud.delete_post(post_id)
    return Response(status=204, data=None)
