from django.db import models


class GoalCategory(models.Model):
    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    user = models.ForeignKey('core.User', verbose_name='Автор', related_name='categories', on_delete=models.PROTECT)
    title = models.CharField(max_length=255, verbose_name='Название')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения')
    is_deleted = models.BooleanField(verbose_name='Удалена', default=False)


class Status(models.IntegerChoices):
    to_do = 1, "К выполнению"
    in_progress = 2, "В процессе"
    done = 3, "Выполнено"
    archived = 4, "Архив"


class Priority(models.IntegerChoices):
    low = 1, "Низкий"
    medium = 2, "Средний"
    high = 3, "Высокий"
    critical = 4, "Критический"


class Goal(models.Model):
    class Meta:
        verbose_name = 'Цель'
        verbose_name_plural = 'Цель'

    title = models.CharField(max_length=255, verbose_name='Заголовок')
    description = models.TextField(verbose_name='Описание')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
    due_date = models.DateField(verbose_name='Дата исполнения')
    user = models.ForeignKey('core.User', related_name='goal_users', verbose_name='Пользователь', on_delete=models.PROTECT)
    category = models.ForeignKey('goals.GoalCategory', related_name='goal_categories', verbose_name='Категория', on_delete=models.PROTECT)
    priority = models.IntegerField(choices=Priority.choices, default=Priority.low, verbose_name='Приоритет')
    status = models.IntegerField(choices=Status.choices, default=Status.to_do, verbose_name='Статус')


class GoalComment(models.Model):
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    text = models.TextField(verbose_name='Текст')
    goal = models.ForeignKey('goals.Goal', related_name='goal_comments', on_delete=models.CASCADE)
    user = models.ForeignKey('core.User', related_name='user_comments', verbose_name='Пользователь',
                             on_delete=models.PROTECT)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    updated = models.DateTimeField(auto_now=True, verbose_name='Изменено')
