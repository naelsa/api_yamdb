from rest_framework import serializers
from rest_framework.fields import IntegerField
from rest_framework.relations import SlugRelatedField

from reviews.models import Review
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

    def create(self, validated_data):
        genres = validated_data.pop('genre')
        category = validated_data.pop('category')
        title = Title.objects.create(
            **validated_data, category=category)
        for genre in genres:
            title.genre.add(genre)
        return title

    def update(self, instance, validated_data):
        Title.objects.filter(id=instance.id).update(**validated_data)
        title = Title.objects.get(id=instance.id)
        return title

    class Meta:
        model = Title
        fields = '__all__'
