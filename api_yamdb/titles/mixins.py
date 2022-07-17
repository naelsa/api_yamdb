from rest_framework.mixins import (
    ListModelMixin, CreateModelMixin, DestroyModelMixin
)
from rest_framework.viewsets import GenericViewSet


class CreateListDestroyViewSet(ListModelMixin,
                               CreateModelMixin,
                               DestroyModelMixin,
                               GenericViewSet):
    pass
