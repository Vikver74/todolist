from django.core.validators import MinLengthValidator
from django.db import models


class TgUser(models.Model):
    tg_chat_id = models.BigIntegerField()
    tg_user_id = models.BigIntegerField(unique=True)
    tg_username = models.CharField(max_length=32, validators=[MinLengthValidator(5)], null=True)
    user = models.ForeignKey('core.User', null=True, on_delete=models.CASCADE)
    verification_code = models.CharField(max_length=32, unique=True)
