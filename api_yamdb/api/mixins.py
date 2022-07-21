from django.contrib import admin
from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet

from .permissions import IsAdminOrReadOnly


class CustomEmptyMixin(admin.ModelAdmin):
    """Кастомный миксин для пустого поля."""
    empty_value_display = '-пусто-'


class CreateListDestroyViewSet(ListModelMixin,
                               CreateModelMixin,
                               DestroyModelMixin,
                               GenericViewSet):
    permission_classes = (IsAdminOrReadOnly,)
    search_fields = ('name',)
    lookup_field = 'slug'
