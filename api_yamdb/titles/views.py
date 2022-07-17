from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend

from .mixins import CreateListDestroyViewSet
from .models import Titles, Genres, Categories
from .permissions import IsAdminOrReadOnly
from .serializers import (TitlesSerializer, GenresSerializer,
                          CategoriesSerializer, TitlesCreateSerializer)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ('genre', 'category', 'name')

    def get_serializer_class(self):
        if self.action == 'create':
            return TitlesCreateSerializer
        if self.action == 'partial_update':
            return TitlesCreateSerializer
        return TitlesSerializer


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        return Genres.objects.get(slug=self.kwargs['pk'])


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        slug = self.kwargs['pk']
        return Categories.objects.get(slug=slug)
