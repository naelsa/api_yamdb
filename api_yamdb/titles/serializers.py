from rest_framework.relations import SlugRelatedField

from .models import Categories, Genres, Titles
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ("id",)


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        exclude = ("id",)


class TitlesSerializer(serializers.ModelSerializer):
    genre = SlugRelatedField(
        slug_field='slug',
        queryset=Genres.objects.all(),
        many=True,
    )
    category = SlugRelatedField(
        slug_field='slug',
        queryset=Categories.objects.all(),
    )

    class Meta:
        model = Titles
        fields = '__all__'


class TitlesObjectSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True,)
    category = CategoriesSerializer()

    class Meta:
        model = Titles
        fields = '__all__'
