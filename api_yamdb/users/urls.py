from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (UserViewSet, signup_user, get_token)

router_v1 = DefaultRouter()

router_v1.register('v1/users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router_v1.urls)),
    path('v1/auth/signup/', signup_user, name='auth_signup'),
    path('v1/auth/token/', get_token, name='token'),
]
