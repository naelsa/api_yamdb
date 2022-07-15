from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, )

router = DefaultRouter()

router.register('v1/users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls)),
    path('v1/auth/signup/', registration_API_view),
    path('v1/auth/token/', take_confirmation_code_view),
]