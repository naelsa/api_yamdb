from django.db import models

from .validators import validate_year


class BaseModel(models.Model):
    """Базовый класс для категорий и жанров."""
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True, max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
        ordering = ['name']


class Categories(BaseModel):
    """Категории (типы) произведений."""
    class Meta(BaseModel.Meta):
        verbose_name = 'Категории'


class Genres(BaseModel):
    """Категории жанров."""
    class Meta(BaseModel.Meta):
        verbose_name = 'Жанры'


class Title(models.Model):
    """Произведения, к которым пишут отзывы."""
    name = models.CharField(max_length=256)
    year = models.IntegerField(validators=[validate_year])
    description = models.CharField(max_length=256, null=True)
    genre = models.ManyToManyField(
        Genres, related_name="titles",
        blank=True
    )
    category = models.ForeignKey(
        Categories, on_delete=models.SET_NULL,
        related_name="titles", blank=True, null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']
        verbose_name = 'Произведения'
