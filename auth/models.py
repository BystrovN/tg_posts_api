import secrets

from django.contrib.auth import get_user_model
from django.db import models


class Token(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    key = models.CharField(max_length=100, unique=True)

    @staticmethod
    def generate_token():
        return secrets.token_hex(20)

    def __str__(self):
        return f'Token for {self.user.username}'
