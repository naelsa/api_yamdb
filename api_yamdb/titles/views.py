from django.db.models import Avg
from rest_framework import viewsets
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

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve',):
            return TitlesSerializer
        return TitlesCreateSerializer


class GenresViewSet(CreateListDestroyViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer


class CategoriesViewSet(CreateListDestroyViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
