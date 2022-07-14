from rest_framework import viewsets
from users.models import User
from users.serializers import UserSerializer
from users.permissions import (IsAdmin, IsModerator,
                               IsSuperuser, IsAdminOrReadOnly)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = ()
