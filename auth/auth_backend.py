from ninja.security import HttpBearer

from .models import Token


class TokenAuth(HttpBearer):
    def authenticate(self, request, token: str):
        try:
            return Token.objects.get(key=token).user
        except Token.DoesNotExist:
            return None
