from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import import (UserViewSet)

router_v1 = DefaultRouter()

router_v1.register('v1/users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/auth/signup/', reg.....),
    path('v1/auth/token/', token.....)
]