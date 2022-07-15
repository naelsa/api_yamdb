from rest_framework import viewsets, status, filters
from rest_framework.decorators import action, api_view
from rest_framework.response import Response

from users.models import User
from users.serializers import (UserSerializer, RegistrationSerializer,
                               RegTokSerializer)
from users.permissions import (IsAdmin, IsModerator,
                               IsSuperuser, IsAdminOrReadOnly)
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny, IsAuthenticated


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated, IsAdmin | IsSuperuser]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('username',)
    lookup_field = 'username'

    @action(methods=['GET', 'PATCH'], detail=False,
            permission_classes=[IsAuthenticated], url_path='me')
    def user_me(self, request):
        if request.method != 'PATCH':
            serializer = self.get_serializer(request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        serializer = self.get_serializer(request.user, data=request.data,
                                         partial=True)
        serializer.is_valid(raise_exception=True)
        if serializer.validated_data.get('role'):
            serializer.validated_data['role'] = request.user.role
        serializer.save()
        return Response(serializer.data)

#
# @api_view(['POST'])
# def signup_user(request):
#     serializer = RegTokSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     username = serializer.validated_data.get('username')
#     email = serializer.validated_data.get('email')
