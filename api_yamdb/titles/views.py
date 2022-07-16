from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Titles, Genres, Categories
from .permissions import IsAdminOrReadOnly
from .serializers import (TitlesSerializer, GenresSerializer,
                          CategoriesSerializer, TitlesObjectSerializer)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)


class TitlesObjectViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesObjectSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_object(self):
        id = self.kwargs.get("id")
        print(f'вот такой id нашел {id}')
        return get_object_or_404(Titles, id=id)


class GenresViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        return get_object_or_404(
            Genres,
            slug=self.kwargs['pk'],
        )


class CategoriesViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        return get_object_or_404(
            Genres,
            slug=self.kwargs['pk'],
        )
