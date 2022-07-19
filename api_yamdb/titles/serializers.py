from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Categories, Genres, Title


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ("id",)
        lookup_field = 'slug'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        exclude = ("id",)
        lookup_field = 'slug'


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True, )
    category = CategoriesSerializer()
    rating = serializers.IntegerField(read_only=True,)

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'rating',
                  'description', 'genre', 'category')


class TitlesCreateSerializer(serializers.ModelSerializer):
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
        model = Title
        fields = '__all__'
