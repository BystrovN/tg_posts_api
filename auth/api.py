from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from ninja import Router

from .models import Token
from .schemas import RegisterSchema, TokenSchema

router = Router(tags=['Auth'])


@router.post('/register/', response={201: TokenSchema, 400: dict}, url_name='token-create')
def register_user(request, data: RegisterSchema):
    if get_user_model().objects.filter(username=data.username).exists():
        return 400, {'error': 'Username already taken'}

    user = get_user_model().objects.create_user(**data.model_dump())
    token = Token.objects.create(user=user, key=Token.generate_token())
    return 201, {'token': token.key}


@router.post('/token/', response={200: TokenSchema, 401: dict}, url_name='token-retrieve')
def get_token(request, data: RegisterSchema):
    user = authenticate(**data.model_dump())
    if not user:
        return 401, {'error': 'Invalid credentials'}

    token, _ = Token.objects.get_or_create(user=user)
    if not token.key:
        token.key = Token.generate_token()
        token.save()

    return {'token': token.key}
