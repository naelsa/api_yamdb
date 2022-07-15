from django.db import models
from django.contrib.auth.models import AbstractUser

from api_yamdb import settings
from .generate_code import generate_confirmation_code


class User(AbstractUser):
    """Кастомный пользователь с дополнительными полями."""
    username = models.CharField(max_length=150,
                                unique=True,
                                verbose_name='Имя пользователя'
                                )
    email = models.EmailField(
        max_length=254,
        unique=True,
        verbose_name='Электронная почта'
    )
    bio = models.TextField(
        blank=True,
        verbose_name='Биография'
    )
    confirmation_code = models.CharField(
        max_length=50,
        blank=True,
        verbose_name='Код для авторизации',
        default=generate_confirmation_code()
    )
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

    role = models.CharField(
        max_length=13,
        choices=settings.USER_ROLE_CHOICES,
        default=settings.USER_ROLE_USER
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    @property
    def is_admin(self):
        return self.role == settings.USER_ROLE_ADMIN or self.is_superuser

    @property
    def is_moderator(self):
        return self.role == settings.USER_ROLE_MODERATOR
