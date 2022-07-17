from django.db.models import Avg
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
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
        rating=Avg('reviews__score')).order_by('id')
    permission_classes = (IsAuthenticatedOrReadOnly, IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    filterset_class = TitleFilter
    pagination_class = PageNumberPagination

    def get_serializer_class(self):
        if self.action in ('create', 'update', 'partial_update'):
            return TitlesCreateSerializer
        return TitlesSerializer


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
