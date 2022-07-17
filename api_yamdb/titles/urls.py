from django.urls import include, path
from rest_framework import routers

from .views import (TitlesViewSet, GenresViewSet, CategoriesViewSet)

v1_router = routers.DefaultRouter()
v1_router.register('genres', GenresViewSet)
v1_router.register('categories', CategoriesViewSet)
v1_router.register('titles', TitlesViewSet)


app_name = 'api'
urlpatterns = [
    path('v1/', include(v1_router.urls)),
]
