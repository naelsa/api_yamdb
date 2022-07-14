from django.db import models
from django.contrib.auth.models import AbstractUser

# from .generate_code import generate_confirmation_code


class User(AbstractUser):
    """Кастомный пользователь с дополнительными полями."""
    username = models.CharField(max_length=150,
                                unique=True,
                                verbose_name='Имя пользователя'
                                )
    email = models.EmailField(
        max_length=254,
        unique=True,
        blank=True,
        verbose_name='Электронная почта'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    # confirmation_code = models.CharField(
    #     max_length=50,
    #     blank=True,
    #     verbose_name='Код для авторизации',
    #     default=generate_confirmation_code()
    # )
    first_name = models.CharField(
        'Имя',
        max_length=150,
        blank=True)
    last_name = models.CharField(
        'Фамилия',
        max_length=150,
        blank=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)

    USER_ROLE_USER = 'user'
    USER_ROLE_MODERATOR = 'moderator'
    USER_ROLE_ADMIN = 'admin'

    USER_ROLE_CHOICES = (
        (USER_ROLE_USER, 'Пользователь'),
        (USER_ROLE_MODERATOR, 'Модератор'),
        (USER_ROLE_ADMIN, 'Админ'),
    )

    role = models.CharField(
        max_length=19,
        choices=USER_ROLE_CHOICES,
        default='user'
    )

