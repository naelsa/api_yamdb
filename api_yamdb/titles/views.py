from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import TitleFilter
from .mixins import CreateListDestroyViewSet
from .models import Title, Genres, Categories
from .permissions import IsAdminOrReadOnly
from .serializers import (TitlesSerializer, GenresSerializer,
                          CategoriesSerializer, TitlesCreateSerializer)


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('name', )
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
    filterset_class = TitleFilter
    ordering_fields = ['name']
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve',):
            return TitlesSerializer
        return TitlesCreateSerializer


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all().order_by('id')
    serializer_class = GenresSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        return Genres.objects.get(slug=self.kwargs['pk'])


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all().order_by('id')
    serializer_class = CategoriesSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)

    def get_object(self, queryset=None):
        slug = self.kwargs['pk']
        return Categories.objects.get(slug=slug)
