from django.urls import include, path
from rest_framework import routers

from .views import TitlesViewSet, GenresViewSet, CategoriesViewSet

v1_router = routers.DefaultRouter()
v1_router.register('titles', TitlesViewSet)
v1_router.register('genres', GenresViewSet)
v1_router.register('categories', CategoriesViewSet)
v1_router.register(r'titles/(?P<id>[\w]+)/', TitlesViewSet,
                   basename="titles")

app_name = 'api'
urlpatterns = [
    path('v1/titles/', include(v1_router.urls)),
    path('v1/genres/', include(v1_router.urls)),
    path('v1/categories/', include(v1_router.urls)),
]