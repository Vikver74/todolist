from django.db import models
from django.utils import timezone

from core.models import User


class GoalCategory(models.Model):
    class Meta:
        verbose_name='Категория'
        verbose_name_plural='Категории'

    user = models.ForeignKey(User, verbose_name='Автор', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)

    # def save(self, *args, **kwargs):
    #     if not self.id:
    #         self.created = timezone.now()
    #     self.updated = timezone.now()
    #
    #     return super().save(*args, **kwargs)
