from django.db import models
from django.conf import settings

from .validators import validate_year


class BaseModel(models.Model):
    """Базовый класс для категорий и жанров."""
    name = models.CharField(max_length=settings.MAX_LENGTH_TITLE_NAME)
    slug = models.SlugField(unique=True, max_length=settings.MAX_LENGTH_SLUG)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ('name',)


class Categories(BaseModel):
    """Категории (типы) произведений."""
    class Meta(BaseModel.Meta):
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Genres(BaseModel):
    """Категории жанров."""
    class Meta(BaseModel.Meta):
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'


class Title(models.Model):
    """Произведения, к которым пишут отзывы."""
    name = models.CharField(max_length=settings.MAX_LENGTH_TITLE_NAME)
    year = models.IntegerField(validators=[validate_year])
    description = models.CharField(
        max_length=settings.MAX_LENGTH_DESCRIPTION, null=True
    )
    genre = models.ManyToManyField(
        Genres, related_name="titles",
        blank=True
    )
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL,
        related_name="titles", blank=True, null=True
    )

    class Meta:
        ordering = ('name',)
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name
