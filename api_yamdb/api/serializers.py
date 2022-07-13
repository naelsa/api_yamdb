from titles.models import Categories, Genres, Titles
from rest_framework import serializers


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = '__all__'
