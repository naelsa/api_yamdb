from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from .models import Categories, Genres, Titles


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        exclude = ("id",)


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        exclude = ("id",)


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True,)
    category = CategoriesSerializer()

    class Meta:
        model = Titles
        fields = '__all__'


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
        title = Titles.objects.create(
            **validated_data, category=category)
        for genre in genres:
            title.genre.add(genre)
        return title

    def update(self, instance, validated_data):
        Titles.objects.filter(id=instance.id).update(**validated_data)
        title = Titles.objects.get(id=instance.id)
        return title

    class Meta:
        model = Titles
        fields = '__all__'
