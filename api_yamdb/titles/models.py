from django.db import models


class Categories(models.Model):
    """Категории (типы) произведений."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    """Категории жанров."""
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Titles(models.Model):
    """Произведения, к которым пишут отзывы."""
    name = models.CharField(max_length=200)
    year = models.IntegerField()
    categorie = models.ForeignKey(
        Categories, on_delete=models.SET_NULL,
        related_name="titles", blank=True, null=True
    )
    genre = models.ManyToManyField(
        Genres, related_name="titles",
        blank=True, null=True
    )

    def __str__(self):
        return self.name
